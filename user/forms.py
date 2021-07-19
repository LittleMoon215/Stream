from django import forms
from django.contrib.auth.models import User


from user.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True, label='username')

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )
        labels = {
            'username': 'Имя пользователя',
            'email': 'E-Mail',
            'password1': 'Пароль',
            'password2': 'Подтвердите пароль'
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return User
