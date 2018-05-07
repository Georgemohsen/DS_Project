from django import forms
from . models import UserProfile, UserData


class EditProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'date_of_birth', 'phone', 'city', 'about', 'photo']


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['title', 'file']
