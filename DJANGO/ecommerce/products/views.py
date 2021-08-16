from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Student, Person
from .forms import PersonForm, ProductForm


def from_app(request):
    return HttpResponse("This is http response from an app")


def second_function(request):
    return HttpResponse("This is http response from an app with second function")


def show_index_page(request):
    return render(request, 'products/index.html')


def second_page(request):
    return render(request, 'products/second.html')


def get_products(request):
    products_django = Product.objects.all()
    context = {
        "products": products_django,
        "activate_product": 'active'
    }
    return render(request, 'products/getProducts.html', context)


def get_person_form(request):
    form_django = PersonForm()
    context = {
        'form': form_django
    }
    return render(request, 'products/get_person_form.html', context)


def get_product_form(request):
    form = ProductForm()
    context = {
        'forms': form
    }
    return render(request, 'products/get_product_form.html', context)


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


def get_students(request):
    students = Student.objects.all()
    context = {
        'students': students,
        'activate_student': 'active'
    }
    return render(request, 'products/get_students.html', context)


def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('/products/get_students/')


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