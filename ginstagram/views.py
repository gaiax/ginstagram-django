from django.views import generic
from django.urls import reverse

from .models import User
from .forms import UserForm, UserIconForm


class Profile(generic.DetailView):
    model = User
    template_name = 'ginstagram/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'


class Registration(generic.edit.CreateView):
    template_name = 'ginstagram/registration.html'
    form_class = UserForm

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
