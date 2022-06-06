from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView


# Create your views here.
# TODO HERE WE ARE MAKING INDIVIDUAL CONCRETE CLASSES TO DEMONSTRATE CONCEPT

# TODO GET DATA API
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# TODO POST DATA API
class StudentPost(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# TODO RETRIEVE DATA API
class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# TODO DESTROY DATA API
class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# TODO UPDATE DATA API
class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
