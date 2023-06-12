import random
import string

from django import forms
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from mainsite.models import History, Number, Winners, Bombed
from mainsite.utils import initialize, stop_game


def generate_random_string(length):
    """生成指定长度的随机字符串"""
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for _ in range(length))


class RegisterForm(forms.Form):
    name = forms.CharField(label='姓名')
    class_number = forms.CharField(label='班级')
    number = forms.FloatField(label='数字')


@login_required()
def index(request):
    number = Number.objects.get(pk=1)
    if number.in_progress:  # 游戏进行中
        return render(request, 'standby.html')
    else:
        return HttpResponseRedirect('/result')


def result(request):
    number = Number.objects.get(pk=1)
    if number.in_progress:  # 游戏进行中
        return HttpResponseRedirect('')
    else:
        winners = list(Winners.objects.all())
        bombed = list(Bombed.objects.all())
        try:
            usernumber = request.user.history.number
        except AttributeError:
            usernumber = '-'
        return render(request, 'show_result.html', {'winners': winners,
                                                    'number': number.number,
                                                    'usernumber': usernumber,
                                                    'bombed': bombed})


def register(request):
    if request.method == 'GET':
        number = Number.objects.get(pk=1)
        if number.in_progress:
            form = RegisterForm
            return render(request, 'register.html', {'forms': form})
        else:
            return HttpResponseRedirect('/result')

    form = RegisterForm(data=request.POST)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        class_number = form.cleaned_data.get('class_number')
        number = form.cleaned_data.get('number')
        try:
            user = User.objects.create_user(username=name, password=generate_random_string(10))
            user.save()
            login(request, user)
        except IntegrityError:
            form.add_error("name", "请勿重复提交")
            return render(request, 'register.html', {'forms': form})
        history = History(user=user, class_number=class_number, number=number)
        history.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'register.html', {'forms': form})


@csrf_exempt
def admin(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/admin?next=game_admin')
    else:
        if request.method == 'GET':
            winners = list(Winners.objects.all())
            return render(request, 'game_admin.html', {'winners': winners})
        else:
            print(request.POST.get('command'))
            if request.POST.get('command') == 'start':
                initialize()
                return JsonResponse({'status': 'success'})
            else:
                stop_game()
                return JsonResponse({'status': 'success'})
