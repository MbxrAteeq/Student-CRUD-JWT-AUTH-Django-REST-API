from .models import Student
from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.

# JWT AUTHENTICATION


# Students CRUD
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@csrf_exempt
def students(request, id=None):

    if request.method=='GET':
        if id is not None:
            # stu = Student.objects.get(id = id)
            stu = get_object_or_404(Student, id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = get_list_or_404(Student)
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)


    if request.method=='POST':
        json_data = request.data
        serrializer = StudentSerializer(data = json_data)
        if serrializer.is_valid():
            serrializer.save()
            return Response({'msg':'Data Saved!'})
        return Response(serrializer.errors)


    if request.method=='PUT':
        stu = get_object_or_404(Student, id=id)
        serrializer = StudentSerializer(stu, data = request.data, partial = True)
        if serrializer.is_valid():
            serrializer.save()
            return Response({'msg':'Data Saved!'})
        return Response({"msg":"Data deleted Successfully"})


    if request.method=='DELETE':
        stu = get_list_or_404(Student, id=id)
        # stu = Student.objects.get(id = id)
        # snippet = Student.get_object(id)
        stu[0].delete()
        return Response({"msg":"Data deleted Successfully"})