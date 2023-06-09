# -*- coding = utf-8 -*-
# @Time : 2023/6/9 12:27
# @Author : tqy, ChatGPT
# @File : utils.py
# @Software : PyCharm
import random

from django.contrib.auth.models import User
from django.db.models import Q, F
from django.db.models.functions import Abs

from mainsite.models import Number, History, Winners


def initialize():
    users = User.objects.exclude(is_superuser=True)
    for user in users:
        user.delete()

    winners = Winners.objects.all()
    for winner in winners:
        winner.delete()

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
    histories = History.objects.exclude(Q(数字__exact=number.number)).order_by(Abs(F('数字') - number.number))[:3]
    for history in histories:
        w = Winners(user=history.user,
                    微信号=history.微信号,
                    数字=history.数字,
                    年级=history.年级,
                    班级=history.班级,
                    delta=abs(history.数字-number.number))
        w.save()
