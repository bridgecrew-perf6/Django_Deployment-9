from pyexpat import model
from django import forms
from django.contrib.auth.models import User     #preloaded model from django
from .models import UserProfileInfoModel        #our own created model


#for fields already present in USER package that we imported in models.py
class UserForm(forms.ModelForm):
    password  = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ('username', 'email', 'password')



#for customized  fields in user package that we created in models.py
class UserProfileForm(forms.ModelForm):
    class Meta:
        model =  UserProfileInfoModel
        fields = ('porfolio_site', 'profile_pic')


