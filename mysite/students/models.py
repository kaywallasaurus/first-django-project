from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=400)


class Certificate(models.Model):
    name = models.CharField(max_length=50)


class Grade(models.Model):
    type = models.CharField(max_length=2)


class Faculty(models.Model):
    name = models.CharField(max_length=75)


class Department(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)


class Student(models.Model):
    full_name = models.CharField(max_length=75)
    grad_year = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.SET("Unknown"))
    certificate = models.ForeignKey(Certificate, on_delete=models.PROTECT)
