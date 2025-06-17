from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Attendance, Marks
from .forms import StudentForm, AttendanceForm, MarksForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})

def attendance_list(request):
    attendance_records = Attendance.objects.select_related('student').all()
    return render(request, 'attendance.html', {'attendance_records': attendance_records})

def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance_form.html', {'form': form})

def marks_list(request):
    marks_records = Marks.objects.select_related('student').all()
    return render(request, 'marks.html', {'marks_records': marks_records})

def marks_create(request):
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marks_list')
    else:
        form = MarksForm()
    return render(request, 'marks_form.html', {'form': form})

def custom_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user_type == 'admin' and user.is_superuser:
                return redirect('admin_dashboard')
            elif user_type == 'student' and not user.is_superuser:
                return redirect('student_dashboard')
            else:
                error = 'Invalid user type for this account.'
        else:
            error = 'Invalid username or password.'
    return render(request, 'registration/custom_login.html', {'error': error})

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')
