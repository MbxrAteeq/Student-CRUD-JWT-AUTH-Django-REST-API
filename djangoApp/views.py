from .models import Student
from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

@api_view(['POST'])
def login(request):
    data = request.data

    if not data['username'] and data['password']:
        return Response({"Msg":"Please enter Username and Password"})

    user = Student.objects.filter(username=data['username'], password=data['password'])
    print(user)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({"Msg":"Logged In", 
        'refresh': str(refresh),
        'access': str(refresh.access_token)})

    return Response({"Msg":"Please enter correct Username and Password"})


# Students CRUD
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
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