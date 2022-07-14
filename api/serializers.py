from .models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'productId', 'customerId', 'total', 'discount', 'subTotal', 'qty']
