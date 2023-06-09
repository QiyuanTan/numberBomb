from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponse

from mainsite.models import History


class Form(ModelForm):
    class Meta:
        model = History
        fields = ['微信号']


@login_required
def index(request):
    return HttpResponse('hello world')


def register(request):
    if request.method == 'GET':
        form = Form()
        return render(request, 'register.html', {'forms': form})

    form = Form(data=request.POST)
    if form.is_valid():
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('code', '')

        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'register.html', {'forms': form})

    else:
        return render(request, 'register.html', {'forms': form})
