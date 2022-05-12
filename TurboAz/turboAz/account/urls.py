from django.urls import path
from . import views
urlpatterns = [
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('sign_up',views.user_register,name='register'),
    path('cabinet',views.cabinet,name='cabinet'),
    ]