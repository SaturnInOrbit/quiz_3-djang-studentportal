from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, 'main/home.html')

def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'main/student_list.html', context)