from rest_framework import viewsets
from . serilizer import Student,StuSerilizer

class StudentView(viewsets.ModelViewSet):
    serializer_class=StuSerilizer
    queryset=Student.objects.all()
