from django import forms

from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """form for user register"""

    username = forms.CharField(min_length=2, max_length=70)

    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())

    first_name = forms.CharField(min_length=2, max_length=70)
    last_name = forms.CharField(min_length=2, max_length=70)

    email = forms.CharField(min_length=2, max_length=70, widget=forms.EmailInput)


    def save(self):

        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


  
