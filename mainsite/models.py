from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class History(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wechat_id = models.CharField(max_length=100, name='微信号')
    number = models.FloatField(name="数字")
    grade = models.PositiveSmallIntegerField(name='年级')
    class_number = models.PositiveSmallIntegerField(name='班级')


class Winners(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wechat_id = models.CharField(max_length=100, name='微信号')
    number = models.FloatField(name="数字")
    grade = models.PositiveSmallIntegerField(name='年级')
    class_number = models.PositiveSmallIntegerField(name='班级')
    delta = models.PositiveSmallIntegerField()


class Number(models.Model):
    number = models.FloatField()
    in_progress = models.BooleanField()

    def __str__(self):
        return str(self.number)
