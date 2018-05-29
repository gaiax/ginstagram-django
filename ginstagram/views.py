from django.views import generic
from django.urls import reverse
from .models import User
from .forms import UserForm


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
