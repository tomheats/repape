from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from accounts.models import UserProfile


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )


class EditAdditionalInfoForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = (
            'description',
            'phone',
            'city',
            'website',
        )
