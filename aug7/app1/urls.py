from django.urls import path
from app1 import views
urlpatterns=[
    path('',views.func1,name="hp"),
    path('create',views.func2,name="cp"),
    path('delete',views.func3,name="dp"),
    path('profile',views.func4,name="pp"),
    path('register',views.func5,name="rp"),
    path('login',views.func6,name="lp"),
    path('logout',views.func7,name="lgp"),
]