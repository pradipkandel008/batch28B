from django.urls import path
from . import views

urlpatterns =[
    path('', views.from_app),
    path('home/', views.second_function),
    path('index/', views.show_index_page),
    path('second/', views.second_page),
    path('products/', views.get_products),
    path('get_person_form/', views.get_person_form),
    path('get_product_form/', views.get_product_form),
    path('get_student_form/', views.get_student_form),
    path('get_students/', views.get_students),
    path('delete_student/<int:student_id>', views.delete_student),
    path('update_student/<int:student_id>', views.update_student),
]