from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Exam(models.Model):
    name = models.CharField(max_length=50)
    discipline = models.CharField(max_length=50)

    def __str__(self):
        return self.name