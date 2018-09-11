# from django import form
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime    



def upload_location(instance, filename):
    PostModel = instance.__class__
    new_id = PostModel.objects.order_by("id").last().id + 1
    return "%s/%s" %(new_id, filename)
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='upload_location', 
            null=True, 
            blank=True,)
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null = True)
    post =  models.TextField(null=True,blank=True)
    likee = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now,blank=True)

class Comments(models.Model):
    comment = models.CharField(max_length=100,null=True, blank=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now,blank=True)


class Like(models.Model):
    count_l = models.IntegerField(default=0,null=True, blank=True,)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    


class Dislike(models.Model):
    count_d = models.IntegerField(default=0, null=True, blank=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


