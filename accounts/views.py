# from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrstionForm
from django.contrib.auth import authenticate,login


def home (request):
    return render(request, 'home.html')

def register(request):
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
                    return redirect('/account')

    else:
        form = RegistrstionForm()
        args = {'form': form}
        return render(request, 'accounts/register.html', args)
        
# Create your views here.
