from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime

# Create your models here.

def upload_location(instance, filename):
    PostModel = instance.__class__
    new_id = PostModel.objects.order_by("id").last().id + 1
    return "%s/%s" %(new_id, filename)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.FileField(upload_to='upload_location',   default='/media/profile.png')
    description = models.CharField(max_length=100, default='',null=True)
    city = models.CharField(max_length=100,default='',null=True)
    dob = models.DateField(("DOB"), default=datetime.date.today)
    mobile = models.IntegerField(default=0)
    
def create_profile(sender, **kwargs):
    if(kwargs['created']):
        user_profile  = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)