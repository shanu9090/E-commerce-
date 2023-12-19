from django.shortcuts import render
from .forms import SignUpForm,LogInForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def sign_up(req):
    if req.method=="POST":
        fm = SignUpForm(req.POST)    # Explicitily Mention because this class is borrowed from UserCreationForm
        if fm.is_valid():
            fm.save()
            messages.success(req,'Successfully signed Up')
            fm=SignUpForm()
            return render(req,'auth1/signup.html',{'fm':fm})
    else:
        fm=SignUpForm()
    return render(req,'auth1/signup.html',{'fm':fm})

def log_in(req):
    if req.method=="POST":
        fm = LogInForm(request=req,data=req.POST)
        if fm.is_valid():
            a=fm.cleaned_data['username']
            b=fm.cleaned_data['password']
            user=authenticate(username=a, password=b)
            if user is not None:
                login(req,user)
                messages.success(req,"successfully logged in")
                fm = LogInForm()
                return render (req,"auth1/login.html",{"fm" : fm})


    else:
        fm = LogInForm()
        return render (req,"auth1/login.html",{"fm" : fm})
    
def log_out(req):
    logout(req)
    messages.success(req,"logged out successfully")
    fm=SignUpForm()
    return render(req,'auth1/signup.html',{'fm':fm})
