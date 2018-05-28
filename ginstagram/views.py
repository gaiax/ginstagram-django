from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http.response import HttpResponse
from .models import Users

def main(request):
    return HttpResponse("Hello!")

def profile(request, user_name):
    """ ユーザー詳細画面がユーザー名前ごとに生成"""
    userInfo = get_object_or_404(Users, username=user_name)
    return render(request,'ginstagram/profile.html',{
        'userInfo': userInfo
    })

def registration(request):
    if request.method == 'GET':
        return render(request, 'ginstagram/registration.html')
    elif request.method == 'POST':
        Users.objects.create(username='TEST_USER_NAME')
        return HttpResponse('POST途中')
