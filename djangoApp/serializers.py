from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    # # id = serializers.BigAutoField(primary_key=True)
    # name = serializers.CharField(max_length=45)
    # grades = serializers.CharField(max_length=45)
    # phoneNumber = serializers.CharField(max_length=13)

    