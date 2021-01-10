from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout



# Create your views here.
def clean_username(self):
    username = self.cleaned_data['username']
    if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
        raise forms.ValidationError(u'Username "%s" is already in use.' % username)
    return username



def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        dUser = User.objects.filter(username=username)
        if  dUser.exists():
            messages.info(request,"User Nay Da Ton Tai")
        else:
            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.info(request,"Dang Ky Thanh Cong")
            return redirect("index")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)

    
    
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"User Name or Password Incorrect")
            return render(request,"login.html",context)

        messages.success(request,"Dang nhap thanh cong")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.success(request,"Ban da dang xuat")
    return redirect("index")
