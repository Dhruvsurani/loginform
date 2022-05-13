import re
from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def Sign_up(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account create successfully')
            fm.save()
    else:
        fm = SignupForm()
    return render(request ,'signup.html',{'form':fm})

def Log_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request,data = request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname , password = upass)
                print(user)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/profile/')
        else:    
            fm = AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

def Profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')


def Log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')