from django.shortcuts import render, redirect
from .models import Student, Group, StudentGroup

def add_student_to_group(request, group_id):
    group = Group.objects.get(pk=group_id)
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student = Student.objects.get(pk=student_id)
        student_group = StudentGroup(student=student, group=group)
        student_group.save()
        return redirect('group_detail', group_id=group_id)
    else:
        students = Student.objects.all()
        return render(request, 'generate/add_student')


class StudentListView:
    pass