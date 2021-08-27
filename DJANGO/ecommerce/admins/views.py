from django.shortcuts import render, redirect
from accounts.auth import admin_only
from products.models import *
from django.contrib.auth.models import User

@admin_only
def homepage(request):
    student = Student.objects.all()
    student_count = student.count()
    person = Person.objects.all()
    person_count = person.count()
    files = FileUpload.objects.all()
    files_count = files.count()
    users = User.objects.all()
    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_staff=1).count()
    context = {
        'student': student_count,
        'person': person_count,
        'file': files_count,
        'user': user_count,
        'admin': admin_count
    }

    return render(request, 'admins/homepage.html', context)


