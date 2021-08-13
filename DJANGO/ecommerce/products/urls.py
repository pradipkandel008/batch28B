from django.urls import path
from . import views

urlpatterns =[
    path('', views.from_app),
    path('home/', views.second_function),
    path('index/', views.show_index_page),
    path('second/', views.second_page),
    path('products/', views.get_products),

    path('get_person_form/', views.get_person_form)
]