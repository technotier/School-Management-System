from django.shortcuts import render
from students.models import Attendance
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view()
def student_attendance(request, student_class, student_id):
    try:
        Attendance.objects.create_attendance(student_class, student_id)
        return Response({"Status": "Success"})
    except Exception as err:
        print(err)
        return Response({"Status": "Failed"})

