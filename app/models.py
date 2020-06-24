from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32, unique=True)
    pwd = models.CharField(max_length=64)
    user_type_choices = (
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP')
    )
    user_type = models.IntegerField(choices=user_type_choices)


class UserToken(models.Model):
    token = models.CharField(max_length=64)
    user = models.OneToOneField(to='User',on_delete=models.CASCADE)
