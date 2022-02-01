from operator import mod
from django.db import models
from django.contrib.auth.models import User




class UserProfileInfoModel(models.Model):
    # there is builtin formpage in User package which has already made username,fn,ln,password,email fields
    user = models.OneToOneField(User, on_delete= models.CASCADE) 

    #customizing wanted field in the form or login page 
    porfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(blank=True, upload_to='profile_pics') # choosefile option on page uploading in media directory


    def __str__(self):
        return self.user.username
        