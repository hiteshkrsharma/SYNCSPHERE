from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='custom_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_create, name='student_create'),
    path('students/edit/<int:id>/', views.student_update, name='student_update'),
    path('students/delete/<int:id>/', views.student_delete, name='student_delete'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/add/', views.attendance_create, name='attendance_create'),
    path('marks/', views.marks_list, name='marks_list'),
    path('marks/add/', views.marks_create, name='marks_create'),
    path('accounts/', include('django.contrib.auth.urls')),  # Add built-in auth URLs
]
