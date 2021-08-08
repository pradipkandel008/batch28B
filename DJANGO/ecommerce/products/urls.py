from django.urls import path
from . import views

urlpatterns =[
    path('', views.from_app),
    path('home/', views.second_function)
]