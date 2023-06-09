# -*- coding = utf-8 -*-
# @Time : 2023/6/9 12:27
# @Author : tqy
# @File : utils.py
# @Software : PyCharm
import random
from django.contrib.auth.models import User
from mainsite.models import Number, History


def initialize():
    users = User.objects.exclude(is_superuser=True)
    for user in users:
        user.delete()

    histories = History.objects.all()
    for history in histories:
        history.delate()

    number = Number.objects.get(pk=1)
    number.number = random.randint(0, 201)
    number.in_progress = True
    number.save()


def stop_game():
    number = Number.objects.get(pk=1)
    number.in_progress = False
    number.save()
