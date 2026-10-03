from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'first_name', 'last_name', 'email', 'course','year', 'section']
    search_fields = ['first_name', 'last_name', 'student_id', 'email']
    list_filter = ['course','year', 'section']