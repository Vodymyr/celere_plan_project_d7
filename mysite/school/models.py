from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Group(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.first_name


class Students_group(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} - {self.group}"
