from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.http.response import HttpResponse
from .models import User
from .forms import UserForm

def profile(request, username):
    """ ユーザー詳細画面がユーザー名前ごとに生成"""
    userInfo = get_object_or_404(User, username=username)
    return render(request,'ginstagram/profile.html',{
        'userInfo': userInfo
    })

def registration(request):
    if request.method == 'GET':
        return render(request, 'ginstagram/registration.html')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if not form.is_valid():
            return render(request, 'ginstagram/registration.html', {'form': form})
        else:
            user = form.save()
            return redirect('ginstagram:profile', username=user.username)
