from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


    
class Photo(models.Model):
    imagedata = models.ImageField(null=True, upload_to="", blank=True)
    like = models.ManyToManyField(User,  related_name='likes',blank=True)
    #like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like", blank=True )
    #like = models.TextField(default= '<i class="far fa-heart"></i> ')
    #already_like = models.BooleanField(default=False)