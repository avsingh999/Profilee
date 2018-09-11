from django.template import RequestContext# from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect, render_to_response,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrstionForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext

def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

def home (request):
    if not request.user.is_authenticated:
        return render(request,'accounts/login.html')
    else:
        return redirect("/Myprofile")
# def loginform(request):
def login_user(request):
    # logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/Myprofile')
        else:
            return render(request,'accounts/login.html')
    elif request.user.is_authenticated:
        return redirect('/Myprofile')
    else:
        return render(request,'accounts/login.html')
        
def register(request):
    if(request.user.is_authenticated):
        return redirect('/Myprofile')
    else:
        if request.method == 'POST':
            form = RegistrstionForm(request.POST)
            if(form.is_valid()):
                user = form.save(commit=False)
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user.set_password(password)
                user.save()
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('/')

        else:
            form = RegistrstionForm()
            args = {'form': form}
            return render(request, 'accounts/register.html', args)
        
# Create your views here.
