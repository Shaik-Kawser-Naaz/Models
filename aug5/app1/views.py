from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'index.html')
def loginV(request):
    if request.user.is_authenticated:
        messages.warning(request,"Mama you already Logged!")
        return redirect('homepage')
    #logout(request)
    if request.method=="POST":
        a=request.POST.get('ip1')
        b=request.POST.get('ip2')
        result=authenticate(request,username=a,password=b)
        if result is not None:
            print(a,b,type(result))
            login(request,result)
            messages.success(request,"Thank you for coming back!")
            return redirect('homepage')
        else:
            messages.error(request,"Please enter the right password")
            return redirect('loginpage')
    return render(request,'login.html')
def profile(request):
    return render(request,'profile.html')
def logoutV(request):
    logout(request)
    messages.info(request,"Mama you already Logged!")
    return redirect('loginpage')



