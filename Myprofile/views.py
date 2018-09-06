from django.views.generic import TemplateView
from django.shortcuts import render, redirect,get_object_or_404, HttpResponse
from django.http import JsonResponse
from .forms import HomeForm, PostsData, postLike
from .models import Post,Comments, Like ,Dislike
from django.template.loader import render_to_string
import json

def HomeView (request):
    template_name = 'home/home.html'
    if request.user.is_staff and request.method == 'POST':
        form = HomeForm(request.POST)
        postcommenting = PostsData(request.POST)
        if form.is_valid():
            post =  form.save(commit=False)
            post.user = request.user
            post.save()
            form = HomeForm()
            return redirect('/Myprofile')
     

        args = {'form': form, 'postcommenting':postcommenting}
        return render(request, template_name, args)
    else:

        form = HomeForm()
        postcommenting = PostsData()
        posts = Post.objects.all()
        comments = Comments.objects.all()        
        args =  {'form':form,'postcommenting':postcommenting,'posts':posts, 'comments':comments}
        return render(request, template_name,args)

def viewpost(request,id):
    posts = get_object_or_404(Post,pk=id)
    comments = Comments.objects.all().filter(post_id=id)

    if request.method == 'GET':
        print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        template_name = 'home/viewpost.html'
        postcommenting = PostsData()
        args =  {'postcommenting': postcommenting,'posts':posts, 'comments':comments,'id':id}
        return render(request, 'home/viewpost.html', args)

    else:
        print("*********************************")
        template_name = 'home/viewpost.html'
        postcommenting = PostsData(request.POST)
        LD = True
        if postcommenting.is_valid():
            print("********* comment **********")
            postcomment =  postcommenting.save(commit=False)
            text = postcommenting.cleaned_data['comment']
            postcomment.user = request.user
            postcomment.post = posts
            postcomment.save()
            postcommenting = PostsData()
            # return render(request, 'home/comment.html',{'text':text})

        else:
            posts = get_object_or_404(Post,pk=id)
            findlike = Like.objects.all().filter(post_id=posts.id,user=request.user)
            print(findlike)
            print("before ", posts.likee)
            if(len(findlike)==0):
                posts.likee+=1
                tolike = Like()
                tolike.count_l = posts.likee
                tolike.user = request.user
                tolike.post = posts
                posts.save()
                tolike.save()
                LD=False
            else:
                posts.likee-=1
                dislike = Dislike()
                dislike.count_d = posts.likee
                dislike.user = request.user
                dislike.post = posts
                dislike.save()
                posts.save()
                LD=True
                findlike.delete()
            print(posts.likee)

        args =  {'postcommenting': postcommenting,'posts':posts,'LD':LD, 'comments':comments,'id':id}
        return render(request, 'home/viewpost.html', args)


