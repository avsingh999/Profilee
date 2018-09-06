from django.contrib import admin
from Myprofile.models import Post,Comments, Like, Dislike

# Register your models here.
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Like)
admin.site.register(Dislike)