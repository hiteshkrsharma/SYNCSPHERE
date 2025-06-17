from django.contrib import admin
from .models import ClassRoom, Student, Attendance, Marks

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age', 'gender', 'course', 'admission_date', 'classroom')
    search_fields = ('name', 'email', 'course')
    list_filter = ('gender', 'course', 'classroom')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'date', 'status')
    list_filter = ('status', 'date', 'student')

@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'subject', 'marks')
    list_filter = ('subject', 'student')
