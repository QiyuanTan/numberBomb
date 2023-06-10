from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class History(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wechat_id = models.CharField(max_length=100, name='wechat_id')
    number = models.FloatField(name="number")
    grade = models.PositiveSmallIntegerField(name='grade')
    class_number = models.PositiveSmallIntegerField(name='class_number')


class Winners(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wechat_id = models.CharField(max_length=100, name='wechat_id')
    number = models.FloatField(name="number")
    grade = models.PositiveSmallIntegerField(name='grade')
    class_number = models.PositiveSmallIntegerField(name='class_number')
    delta = models.PositiveSmallIntegerField()


class Number(models.Model):
    number = models.FloatField()
    in_progress = models.BooleanField()

    def __str__(self):
        return str(self.number)
