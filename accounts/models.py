from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100,default='')
    dob = models.DateField(("DOB"), default=datetime.date.today)
    mobile = models.IntegerField(default=0)
    
def create_profile(sender, **kwargs):
    if(kwargs['created']):
        user_profile  = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)