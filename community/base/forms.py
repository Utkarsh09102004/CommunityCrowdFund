from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
from Levenshtein import distance


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'aadhar_number', 'phone_number']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        # Check if the username is the same as first name or last name
        if username and (username == first_name or username == last_name):
            raise forms.ValidationError(
                "Username cannot be the same as first name or last name."
            )

        # Check for similarity between username and first name or last name
        if username and (
                distance(username.lower(), first_name.lower()) < 3 or
                distance(username.lower(), last_name.lower()) < 3
        ):
            raise forms.ValidationError(
                "Username cannot be too similar to first name or last name."
            )

        return cleaned_data


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'