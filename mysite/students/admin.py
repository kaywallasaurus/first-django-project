from django.contrib import admin
from django.contrib import admin
from .models import School, Certificate, Grade, Faculty, Department, Student

admin.site.register(School)
admin.site.register(Certificate)
admin.site.register(Grade)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Student)
