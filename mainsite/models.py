from django.db import models


# Create your models here.
class History(models.Model):
    wechat_id = models.CharField(max_length=100, name='微信号')
    name = models.CharField(max_length=40, name="姓名")
    number = models.IntegerField(name="数字")
    grade = models.PositiveSmallIntegerField(name='年级')
    class_number = models.PositiveSmallIntegerField(name='班级')
