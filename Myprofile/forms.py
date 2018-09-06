from django import forms
from .models import Post,Comments,Like

class HomeForm(forms.ModelForm):
    post = forms.CharField()
    
    class Meta:
        model = Post
        fields = ('post',)

class PostsData(forms.ModelForm):
    comment = forms.CharField()
    class Meta:
        model = Comments
        fields = ('comment',)

class postLike(forms.ModelForm):
    
    class Meta:
        model = Like
        fields = '__all__' 