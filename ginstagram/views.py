from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import ContactForm
from django.http.response import HttpResponse

def main(request):
    return HttpResponse("Hello!")

def login(request):
    template = loader.get_template('ginstagram/login.html')
    context = {}
    form = ContactForm()

    return render(request, template, {
        'form': form,
    })
 
def profile(request, user_name):
    return render(
               request, 
               'ginstagram/profile.html', 
               {'userInfo': user_name} 
            )
