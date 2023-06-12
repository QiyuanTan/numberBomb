# -*- coding = utf-8 -*-
# @Time : 2023/6/9 12:27
# @Author : tqy, ChatGPT
# @File : utils.py
# @Software : PyCharm
import random

from django.contrib.auth.models import User
from django.db.models import Q, F
from django.db.models.functions import Abs

from mainsite.models import Number, History, Winners, Bombed


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
    number.number = round(200 * random.random(), 1)
    number.in_progress = True
    number.save()


def stop_game():
    number = Number.objects.get(pk=1)
    number.in_progress = False
    number.save()
    histories = History.objects.exclude(Q(number__exact=number.number)).order_by(Abs(F('number') - number.number))[:10]
    bombed = History.objects.filter(number=number)
    for history in histories:
        w = Winners(user=history.user,
                    number=history.number,
                    class_number=history.class_number,
                    delta=abs(history.number - number.number))
        w.save()

    for b in bombed:
        w = Bombed(user=b.user,
                   number=b.number,
                   class_number=b.class_number,
                   )
        w.save()
