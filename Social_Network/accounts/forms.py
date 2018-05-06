from django import forms
from . models import UserProfile


class EditProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'date_of_birth', 'phone', 'city', 'about', 'photo']