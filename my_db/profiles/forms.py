from django import forms
from django.contrib.auth import get_user_model
from .models import UserInformation

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form_password'
            }
        )
    )

    def clean_username(self):
        profile = self.cleaned_data.get('username')
        queryset = User.objects.filter(username__iexact=profile)
        if not queryset.exists():
            raise forms.ValidationError('Неправильно ввели имя пользователья или пароль')

        return profile

class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=False)
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form_password'
            }
        )
    )


    def clean_username(self):
        profile = self.cleaned_data.get('username')
        queryset = User.objects.filter(username__iexact=profile)

        if queryset.exists():
            raise forms.ValidationError('Такой пользователь уже существует')
        return profile

class ProfilesModelForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = [
            'name',
            'surname',
            'bio',
            'post',
            'profile_image'
        ]
