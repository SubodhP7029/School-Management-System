from django.shortcuts import render
from django.http import HttpResponse
from Student.forms import StudentForm
from .models import Student
from django.contrib import messages


def home(request):
    return render(request, 'Home/index.html')


def student_register(request):
    student_form = Student.objects.all()
    form = StudentForm(request.POST or None)
    context ={
        "student_form":student_form, 
        "form":form,
    }
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()
            messages.success(request, "Student added successfully")

    else:
        form = StudentForm()
    return render(request,"Student/student_registration.html",context)

