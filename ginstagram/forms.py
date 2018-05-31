import re
from django import forms
from django.core.validators import MinLengthValidator

from .models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(validators=[MinLengthValidator(8)])

    class Meta:
        model = User
        fields = ("username", "password")

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not re.search(r'\d', password):
            raise forms.ValidationError('数字が含まれていません')
        if not re.search(r'[a-zA-Z]', password):
            raise forms.ValidationError('アルファベットが含まれていません')
        return password


class UserIconForm(forms.ModelForm):
    icon = forms.ImageField()

    class Meta:
        model = User
        fields = ("icon",)

    def form_valid(self, form):
        myfile = self.get_form_kwargs().get('files')['icon']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        path = os.path.join(settings.MEDIA_ROOT, 'image', myfile.name)

        destination = open(path, 'wb')
        for chunk in myfile.chunks():
            destination.write(chunk)


