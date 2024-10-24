from django.urls import path
from app1 import views 


urlpatterns=[
    path('',views.home,name="homepage"),
    path('login',views.loginV,name="loginpage"),
    path('profile',views.profile,name="profilepage"),
    path('logout',views.logoutV,name="logoutpage"),

]