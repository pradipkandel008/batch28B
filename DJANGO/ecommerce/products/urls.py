from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('', views.from_app),
    path('home/', views.second_function),
    path('index/', views.show_index_page),
    path('second/', views.second_page),
    path('products/', views.get_products),
    # path('get_person_form/', views.get_person_form),
    path('get_product_form/', views.get_product_form),

    path('get_student_form/', views.get_student_form),
    path('get_students/', views.get_students),
    path('delete_student/<int:student_id>', views.delete_student),
    path('update_student/<int:student_id>', views.update_student),

    path('get_person_form/', views.get_person_form),
    path('get_persons/', views.get_all_person),
    path('delete_person/<int:person_id>', views.delete_person),
    path('update_person/<int:person_id>', views.update_person),

    path('post_file/', views.post_file),
    path('get_files/', views.get_file),
    path('delete_file/<int:file_id>', views.delete_file),
    path('update_file/<int:file_id>', views.update_file),

    path('get_file_modelform/', views.get_file_modelform),
    path('post_file_modelform/', views.post_file_modelform),
    path('delete_file_modelform/<int:file_id>', views.delete_file_modelform),
    path('update_file_modelform/<int:file_id>', views.update_file_modelform),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
