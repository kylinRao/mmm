#coding=utf-8
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template.context_processors import csrf
# Create your views here.

#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from users.models import User
from django import forms
from django.contrib.auth.hashers import make_password, check_password



#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())
#登录
#@csrf_protect
def login(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            dbPassword = User.objects.filter(email = username)[0].password
            #获取的表单数据与数据库进行比较
            if check_password(password, dbPassword):
                return render_to_response('success.html',{'username':username})
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf})
