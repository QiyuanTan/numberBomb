from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import render
from django.http import HttpResponse

from mainsite.models import History


class RegisterForm(forms.Form):
    wechat_id = forms.CharField(label='微信号')
    name = forms.CharField(label='姓名')
    grade = forms.CharField(label='年级')
    class_number = forms.CharField(label='班级')
    number = forms.CharField(label='数字')


@login_required
def index(request):
    return HttpResponse('hello world')


def register(request):
    if request.method == 'GET':
        form = RegisterForm
        return render(request, '../user/templates/templates/register.html', {'forms': form})

    form = RegisterForm(data=request.POST)
    if form.is_valid():
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('code', '')

        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, '../user/templates/templates/register.html', {'forms': form})

    else:
        return render(request, '../user/templates/templates/register.html', {'forms': form})
