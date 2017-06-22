from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # 이 User모델을 AUTH_USER_MODEL로 사용하도록 settings.py에 설정
    """
    동작
    follow : 내가 다른사람을 follow 함
    unfollow : follow 취소

    속성
    follower : 나를 follow 하고 있는 사람
    followers : 나를 follow 하고 있는 사람들
    following : 내가 follow 하고 있는 사람
    friend : 서로 follow 하고 있는 관계
    friends : 서로 follow 하고 있는 모든 관계
    """
    nickname = models.CharField(max_length=24, null=True, unique=True)
    relations = models.ManyToManyField(
        'self',
        through='Relation',
        symmetrical=False,
    )

    def __str__(self):
        return self.nickname or self.username


class Relation(models.Model):
    from_user = models.ForeignKey(User, related_name='follow_relations')
    to_user = models.ForeignKey(User, related_name='follower_relations')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Relation from({}) to({})'.format(
            self.from_user, self.to_user
        )

    def follow(self, user):
        if not isinstance(user, User):
            raise ValueError('"user"argument must <User> class')
        self.follow_relations.get_or_create(to_user=user)

    def unfollow(self, user):
        self.follow_relations.filter(to_user=user).delete()

    def follow_toggle(self, user):
        relation, relation_created = self.follow_relations.get_or_create(to_user=user)
        if not relation_created:
            relation.delete()
        else:
            return relation

    @property
    def following(self):
        relations = self.follow_relations.all()
        return User.objects.filter(pk__in=relations.values('pk'))

    @property
    def followers(self):
        relations = self.follower_relations.all()
        return User.objects.filter(pk__in=relations.values('pk'))

    def is_follow(self, user):
        return self.follow_relations.filter(to_user=user).exists()

    def is_folloew(self, user):
        return self.follower_relations.filter(from_user=user).exists()

    class Meta:
        unique_together = (
            ('from_user', 'to_user'),
        )
