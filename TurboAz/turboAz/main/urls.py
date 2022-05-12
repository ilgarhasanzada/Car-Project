from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('car_detail/<int:id>',views.car_detail,name='car_detail'),
    path('add_car',views.add_car,name='add_car'),
    path('car_filter/<int:id>',views.car_filter,name='car_filter'),
    path('model_filter/<int:id>',views.model_filter,name='model_filter'),
]
