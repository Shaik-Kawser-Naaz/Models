from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.hbb
def func1(request):
    return render(request,'home.html')
def func2(request):
    if request.method=="POST":
        i=request.POST.get('pname')
        print(i)
    return render(request,'create.html')
def func3(request):
    return render(request,'delete.html')
def func4(request):
    return render(request,'profile.html')
def func5(request):
    if request.method=="POST":
        c=request.POST.get('usname')
        d=request.POST.get('lname')
        e=request.POST.get('fname')
        f=request.POST.get('mail')
        g=request.POST.get('passwd')
        h=request.POST.get('cpass')
        print(c,d,e,f,g,h)
        if User.objects.filter(username=usname).exists():
            return redirect('rp') 
        if len(passwd)<=8:
            return redirect('rp')
        if (cpass!=passwd):
            return redirect('rp')
        obj=User.objects.create_user(username=usname,first_name=fname,last_name=lname,email=mail,password=passwd)
        obj.save()
        return redirect('lp')

    return render(request,'register.html')
def func6(request):
    if request.user.is_authenticated:
        return redirect('hp')
    if request.method=="POST":
        a=request.POST.get('kname')
        b=request.POST.get('kpass')
        print(a,b)
        result=authenticate(request,username=a,password=b)
        if result is not None:
            login(request,result)
            if request.user.is_superuser:
               return redirect('/admin')
            else:
               return redirect('lp')    
    return render(request,'login.html')
def func7(request):
    return render(request,'login.html')
