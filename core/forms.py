from django import forms
from .models import Student, Attendance, Marks

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'subject', 'marks']
