from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from account.forms import loginForm, userForm
from main.models import Car

# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('cabinet')
    if request.method=='POST':
        form=loginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                return redirect('cabinet')
    else:   
        form=loginForm()
    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('home')
def user_register(request):
    form=userForm()
    if request.method=='POST':
        form=userForm(request.POST)
        if form.is_valid:
            user=form.save(commit=False)
            user.save()
            login(request,user)
            return redirect('home')
    return render(request,'register.html',{'form':form})
def cabinet(request):
    cars=Car.objects.filter(creator=request.user)
    return render(request,'cabinet.html',{'cars':cars})
