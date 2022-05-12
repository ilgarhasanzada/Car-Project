import re
from django.shortcuts import redirect, render
from .models import Car, Marka,Model
from .forms import carForm, edit_Car
def home(request):
    markas=Marka.objects.all().order_by("marka_name")
    cars=Car.objects.all().order_by("date_time")
    for car in cars:
        car.engine=float(car.engine/1000)
        car.engine=str(car.engine)+' L'
        car.price=str(car.price)+' $'
    return render(request,'home.html',{"cars":cars,"markas":markas})
def car_detail(request,id):
    car=Car.objects.get(id=id)
    if car.is_new==True:
        car.is_new='Yes'
    else:
        car.is_new='No'
    car.price=str(car.price)+' $'
    return render(request,'car_detail.html',{"car":car})
def add_car(request):
    if request.user.is_authenticated:
        print(request.user)
        form=carForm()
        if request.method=="POST":
            form=carForm(request.POST,request.FILES)
            if form.is_valid:
                form.save()
                return redirect('home')
        return render(request,'add_car.html',{"form":form})
    else:
        return redirect("login")
def add_detail(request):
    return render(request,'add_detail.html')
def car_filter(request,id):
    markas=Marka.objects.all().order_by('marka_name')
    marka=Marka.objects.get(id=id)
    cars=Car.objects.filter(marka_name=marka)
    models=Model.objects.filter(marka_name=marka).order_by('model_name')
    for car in cars:
        car.engine=float(car.engine/1000)
        car.engine=str(car.engine)+' L'
        car.price=str(car.price)+' $'
    return render(request,'car_filter.html',{"cars":cars,"markas":markas,'models':models})
def model_filter(request,id):
    
    markas=Marka.objects.all().order_by('marka_name')
    model=Model.objects.get(id=id)
    cars=Car.objects.filter(model_name=model)
    for car in cars:
        car.engine=float(car.engine/1000)
        car.engine=str(car.engine)+' L'
        car.price=str(car.price)+' $'
    return render(request,'model_filter.html',{"cars":cars,"markas":markas,"model":model})
