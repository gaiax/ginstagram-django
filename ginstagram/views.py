import os

from django.views import generic
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404, render
from django.conf import settings

from .models import User
from .forms import UserForm, UserIconForm


class Profile(generic.DetailView):
    model = User
    template_name = 'ginstagram/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'


class Registration(generic.edit.FormView):
    template_name = 'ginstagram/registration.html'
    form_class = UserForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        form = self.get_form()
        return reverse(
            'ginstagram:profile',
            kwargs={'username': form.data.get('username')}
        )


class ProfileIcon(generic.edit.UpdateView):
    model = User
    template_name = 'ginstagram/profile_icon.html'
    form_class = UserIconForm
    slug_field = 'username'
    slug_url_kwarg = 'username'


def upload_file(request, username):
    if request.method == 'POST':
        form = UserIconForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['icon']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            path = os.path.join(settings.MEDIA_ROOT, 'image', myfile.name)

            destination = open(path, 'wb')
            for chunk in myfile.chunks():
                destination.write(chunk)

            user = User.objects.get(username=username)
            user.icon = myfile
            user.save()

        return render(request, 'ginstagram/profile_icon.html', {'username': username, 'form': form})
    else:
        form = UserIconForm()
    return render(request, 'ginstagram/profile_icon.html', {'username': username, 'form': form})


