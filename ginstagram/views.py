from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.http.response import HttpResponse
from django.views import generic
from .models import User
from .forms import UserForm


class Profile(generic.DetailView):
    model = User
    template_name = 'ginstagram/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

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
