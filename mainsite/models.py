from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class History(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.FloatField(name="number")
    class_number = models.CharField(name='class_number', max_length=10)


class Winners(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.FloatField(name="number")
    class_number = models.CharField(name='class_number', max_length=10)
    delta = models.FloatField()


class Bombed(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.FloatField(name="number")
    class_number = models.CharField(name='class_number', max_length=10)


class Number(models.Model):
    number = models.FloatField()
    in_progress = models.BooleanField()

    def __str__(self):
        return str(self.number)
