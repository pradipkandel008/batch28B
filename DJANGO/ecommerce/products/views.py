from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Student, Person, FileUpload
from .forms import PersonForm, ProductForm, FileForm
import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.auth import user_only, admin_only


def from_app(request):
    return HttpResponse("This is http response from an app")


def second_function(request):
    return HttpResponse("This is http response from an app with second function")


def show_index_page(request):
    return render(request, 'products/index.html')


def second_page(request):
    return render(request, 'products/second.html')


@login_required
@user_only
def get_products(request):
    products_django = Product.objects.all()
    context = {
        "products": products_django,
        "activate_product": 'active'
    }
    return render(request, 'products/getProducts.html', context)


# def get_person_form(request):
#     form_django = PersonForm()
#     context = {
#         'form': form_django
#     }
#     return render(request, 'products/get_person_form.html', context)

@login_required
@admin_only
def get_product_form(request):
    form = ProductForm()
    context = {
        'forms': form
    }
    return render(request, 'products/get_product_form.html', context)

@login_required
@admin_only
def get_student_form(request):
    if request.method == 'POST':
        data = request.POST
        firstname1 = data['firstname']
        lastname1 = data['lastname']
        batch1 = data['batch']
        image_url1 = data['img_url']

        student = Student.objects.create(firstname=firstname1,
                                         lastname=lastname1,
                                         batch=batch1,
                                         image_url=image_url1)
        if student:

            return redirect('/products/get_students/')
        # url path
        else:
            return HttpResponse("Unable to create student")
    context = {
        'activate_student': 'active'
    }
    return render(request, 'products/get_student_form.html', context)
    # html file path

@login_required
@admin_only
def get_students(request):
    students = Student.objects.all().order_by('-id')
    context = {
        'students': students,
        'activate_student': 'active'
    }
    return render(request, 'products/get_students.html', context)

@login_required
@admin_only
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('/products/get_students/')

@login_required
@admin_only
def update_student(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == "POST":
        # data = request.POST
        student.firstname = request.POST['firstname']
        student.lastname = request.POST['lastname']
        student.batch = request.POST['batch']
        student.image_url = request.POST['img_url']
        student.save()
        return redirect('/products/get_students/')

    context = {
        'student': student,
        'activate_student': 'active'
    }
    return render(request, 'products/update_student_form.html', context)


# with modelform
@login_required
@admin_only
def get_person_form(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Person Added Successfully')
            return redirect('/products/get_persons/')
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return render(request, 'products/get_person_form.html', {'form_person': form})
    context = {
        'form_person': form,
        'activate_person': 'active'
    }
    return render(request, 'products/get_person_form.html', context)

@login_required
@admin_only
def get_all_person(request):
    persons = Person.objects.all().order_by('-id')
    context = {
        'persons': persons,
        'activate_person': 'active'
    }
    return render(request, 'products/get_persons.html', context)

@login_required
@admin_only
def delete_person(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.add_message(request, messages.SUCCESS, 'Person Deleted Successfully')
    return redirect('/products/get_persons/')

@login_required
@admin_only
def update_person(request, person_id):
    person = Person.objects.get(id=person_id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/products/get_persons/')
    context = {
        'form_person': PersonForm(instance=person),
        'activate_person': 'active'
    }
    return render(request, 'products/update_person.html', context)


# file upload with normal form
@login_required
@admin_only
def post_file(request):
    if request.method == "POST":
        title1 = request.POST['title']
        image1 = request.FILES['file']
        file_obj = FileUpload(title=title1,
                              file=image1)
        file_obj.save()
        if file_obj:
            return redirect('/products/get_files/')
        else:
            return HttpResponse("File could not be uploaded")

    context = {
        'activate_file': 'active'
    }
    return render(request, 'products/post_file.html', context)

@login_required
@admin_only
def get_file(request):
    files = FileUpload.objects.all()
    context = {
        'files': files,
        'activate_file': 'active'
    }
    return render(request, 'products/get_files.html', context)

@login_required
@admin_only
def delete_file(request, file_id):
    image = FileUpload.objects.get(id=file_id)
    os.remove(image.file.path)
    image.delete()
    return redirect('/products/get_files/')

@login_required
@admin_only
def update_file(request, file_id):
    image = FileUpload.objects.get(id=file_id)

    if request.method == "POST":
        if request.FILES.get('file'):
            os.remove(image.file.path)
            image.title = request.POST['title']
            image.file = request.FILES['file']
            image.save()

        else:
            image.title = request.POST['title']
            image.save()
        return redirect('/products/get_files')

    context = {
        'file': image,
        'activate_file': 'active'
    }
    return render(request, 'products/update_file.html', context)

@login_required
@admin_only
def get_file_modelform(request):
    files = FileUpload.objects.all().order_by('-id')
    context = {
        'files': files,
        'activate_file_modelform': 'active'
    }
    return render(request, 'products/get_file_modelform.html', context)

@login_required
@admin_only
def post_file_modelform(request):
    form =  FileForm()
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/products/get_file_modelform/')
        else:
            return HttpResponse("File could not be saved")
    context = {
        'form_file': form,
        'activate_file_modelform': 'active'
    }
    return render(request, 'products/post_file_modelform.html', context)

@login_required
@admin_only
def delete_file_modelform(request, file_id):
    image = FileUpload.objects.get(id=file_id)
    os.remove(image.file.path)
    image.delete()
    return redirect('/products/get_file_modelform/')

@login_required
@admin_only
def update_file_modelform(request, file_id):
    file = FileUpload.objects.get(id=file_id)
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
            return redirect('/products/get_file_modelform/')
        else:
            return HttpResponse("File could not be saved")
    context = {
        'form_file': FileForm(instance=file),
        'activate_file_modelform': 'active'
    }
    return render(request, 'products/update_file_modelform.html', context)


@login_required
@user_only
def show_students(request):
    students = Student.objects.all().order_by('-id')
    context = {
        'students': students
    }
    return render(request, 'products/show_students.html', context)