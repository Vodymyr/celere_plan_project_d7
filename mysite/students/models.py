from django.db import models
from django.core.exceptions import ValidationError
import re

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)

    def clean(self):
        super().clean()

        if not re.match(r'^\+?1?\d{9,15}$', self.phone):
            raise ValidationError('Введіть коректний номер телефону')
    def __str__(self):
        return self.first_name

class StudentsGroup(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.first_name} - {self.group.name}"