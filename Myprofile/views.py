from django.views.generic import TemplateView
from django.shortcuts import render, redirect,get_object_or_404, HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import HomeForm, PostsData, postLike
from .models import Post,Comments, Like ,Dislike
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from accounts.models import UserProfile

import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def HomeView (request):
    template_name = 'home/home.html'
    userinfo = UserProfile.objects.all().filter(user=request.user)
    print(userinfo[0])
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = HomeForm(request.POST, request.FILES)
            postcommenting = PostsData(request.POST)
            if form.is_valid():
                post =  form.save(commit=False)
                print("*********************************")
                print(form.cleaned_data["image"],form.cleaned_data["post"])
                print("*********************************")
                # post.image = request.POST['image']
                if form.cleaned_data["image"] is None and form.cleaned_data["post"]=='':
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                post.user = request.user
                post.save()
                print(post.image)
                form = HomeForm()
                return redirect('/Myprofile')
            args = {'form': form, 'postcommenting':postcommenting}
            return render(request, template_name, args)
        else:
            form = HomeForm()
            postcommenting = PostsData()
            posts = Post.objects.all()
            comments = Comments.objects.all()  
            posts=posts[::-1]
            page = request.GET.get('page', 1)
            paginator = Paginator(posts, 6)
            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)
            print(userinfo)
            args =  {'form':form,'postcommenting':postcommenting,'posts':posts, 'comments':comments, 'userinfo':userinfo[0]}
            return render(request, template_name,args)
    else:
        return redirect('/')

def viewpost(request,id):
    if request.user.is_authenticated:
        posts = get_object_or_404(Post,pk=id)
        comments = Comments.objects.all().filter(post_id=id)
        findlike = Like.objects.all().filter(post_id=posts.id,user=request.user)

        if request.method == 'GET':
            template_name = 'home/viewpost.html'
            postcommenting = PostsData()
            if(len(findlike)==0):
                args =  {'postcommenting': postcommenting,'posts':posts, 'comments':comments,'id':id, "like":True}
            else:
                args =  {'postcommenting': postcommenting,'posts':posts, 'comments':comments,'id':id, "like":False}

            return render(request, 'home/viewpost.html', args)
    else:
        return redirect('/')

    # else:
    #     print("*********************************")
    #     print(request.user.is_authenticated)
    #     template_name = 'home/viewpost.html'
    #     postcommenting = PostsData(request.POST)
    #     LD = True
    #     if postcommenting.is_valid():
    #         print("********* comment **********")
    #         postcomment =  postcommenting.save(commit=False)
    #         text = postcommenting.cleaned_data['comment']
    #         postcomment.user = request.user
    #         postcomment.post = posts
    #         postcomment.save()
    #         postcommenting = PostsData()
    #         # return render(request, 'home/comment.html',{'text':text})

    #     else:
    #         posts = get_object_or_404(Post,pk=id)
    #         findlike = Like.objects.all().filter(post_id=posts.id,user=request.user)
    #         print(findlike)
    #         print("before ", posts.likee)
    #         if(len(findlike)==0):
    #             posts.likee+=1
    #             tolike = Like()
    #             tolike.count_l = posts.likee
    #             tolike.user = request.user
    #             tolike.post = posts
    #             posts.save()
    #             tolike.save()
    #             LD=False
    #         else:
    #             posts.likee-=1
    #             dislike = Dislike()
    #             dislike.count_d = posts.likee
    #             dislike.user = request.user
    #             dislike.post = posts
    #             dislike.save()
    #             posts.save()
    #             LD=True
    #             findlike.delete()
    #         print(posts.likee)

    #     args =  {'postcommenting': postcommenting,'posts':posts,'LD':LD, 'comments':comments,'id':id}
    #     return render(request, 'home/viewpost.html', args)



def commentpost(request,id):
    if request.user.is_authenticated:
        posts = get_object_or_404(Post,pk=id)
        comments = Comments.objects.all().filter(post_id=id)
        if request.method == 'POST':
            print(request.user.is_authenticated)
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
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('/')