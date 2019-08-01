from django.urls import path
from . import views

urlpatterns = [
    path('attendance/<student_class>/<student_id>', views.student_attendance, name='student_attendance'),
]

