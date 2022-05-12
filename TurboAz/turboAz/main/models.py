from distutils.command.upload import upload
from imp import reload
from django.db import models

from account.models import CustomUser
# Create your models here.
class Marka(models.Model):
    marka_name=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.marka_name
class Model(models.Model):
    marka_name=models.ForeignKey(Marka,on_delete=models.CASCADE)
    model_name=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.model_name
class Oturucu(models.Model):
    oturucu_teker=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.oturucu_teker
class Suretler_qutusu(models.Model):
    suretler_qutusu=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.suretler_qutusu
class Color(models.Model):
    color=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.color
class Yanacaq(models.Model):
    yanacaq=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.yanacaq
class Car(models.Model):
    marka_name=models.ForeignKey(Marka,on_delete=models.CASCADE,null=True,blank=True)
    model_name=models.ForeignKey(Model,on_delete=models.CASCADE,null=True,blank=True)
    creator=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    year=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    distange=models.PositiveIntegerField()
    engine=models.PositiveIntegerField()
    choose=models.BooleanField(default=False)
    is_new=models.BooleanField(default=False)
    date_time=models.DateField(auto_now_add=True,null=True)
    car_image=models.ImageField(upload_to='cars')
    city=models.CharField(max_length=200)
    yanacaq=models.ForeignKey(Yanacaq,on_delete=models.CASCADE)
    oturucu_teker=models.ForeignKey(Oturucu,on_delete=models.CASCADE)
    suretler_qutusu=models.ForeignKey(Suretler_qutusu,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return "{} {}".format(self.marka_name,self.model_name)