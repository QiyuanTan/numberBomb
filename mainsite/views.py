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

from mainsite.models import History, Number, Winners
from mainsite.utils import initialize, stop_game


def generate_random_string(length):
    """生成指定长度的随机字符串"""
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for _ in range(length))


class RegisterForm(forms.Form):
    wechat_id = forms.CharField(label='微信号')
    name = forms.CharField(label='姓名')
    grade = forms.IntegerField(label='年级')
    class_number = forms.IntegerField(label='班级')
    number = forms.FloatField(label='数字')


@login_required
def index(request):
    number = Number.objects.get(pk=1)
    if number.in_progress:  # 游戏进行中
        return render(request, 'standby.html')
    else:  # 显示结果
        winners = list(Winners.objects.all())
        return render(request, 'show_result.html', {'winners': winners})


def register(request):
    if request.method == 'GET':
        form = RegisterForm
        return render(request, 'register.html', {'forms': form})

    form = RegisterForm(data=request.POST)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        wechat_id = form.cleaned_data.get('wechat_id')
        grade = form.cleaned_data.get('grade', '')
        class_number = form.cleaned_data.get('class_number')
        number = form.cleaned_data.get('number')
        try:
            user = User.objects.create_user(username=name, password=generate_random_string(10))
            user.save()
            login(request, user)
        except IntegrityError:
            form.add_error("name", "请勿重复提交")
            return render(request, 'register.html', {'forms': form})
        history = History(user=user, 微信号=wechat_id, 年级=grade, 班级=class_number, 数字=number)
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
            return render(request, 'game_admin.html')
        else:
            print(request.POST.get('command'))
            if request.POST.get('command') == 'start':
                initialize()
                return JsonResponse({'status': 'success'})
            else:
                stop_game()
                return JsonResponse({'status': 'success'})
