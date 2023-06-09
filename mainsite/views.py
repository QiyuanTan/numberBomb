from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from mainsite.models import History
import random
import string
from django.db import IntegrityError


def generate_random_string(length):
    """生成指定长度的随机字符串"""
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for _ in range(length))


class RegisterForm(forms.Form):
    wechat_id = forms.CharField(label='微信号')
    name = forms.CharField(label='姓名')
    grade = forms.IntegerField(label='年级')
    class_number = forms.IntegerField(label='班级')
    number = forms.IntegerField(label='数字')


@login_required
def index(request):
    return HttpResponse('hello world')


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
        print(wechat_id)
        try:
            user = User.objects.create_user(username=name, password=generate_random_string(10))
            user.save()
        except IntegrityError:
            form.add_error("name", "请勿重复提交")
            return render(request, 'register.html', {'forms': form})

        history = History(user=user, wechat_id=wechat_id)
        history.save()
    else:
        return render(request, 'register.html', {'forms': form})
