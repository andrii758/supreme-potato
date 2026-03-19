from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    # add email field and make him required
    email = forms.EmailField(required=True)

    # list upon registration, didn't add others because it's not required for first registration
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


# fields to update profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "avatar",
            "banner",
            "bio",
            "location",
            "website",
        ]
