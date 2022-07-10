from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Course
from user import serializers
from user.models import CustomUser
from user.serializers import UserSerializer,StudentSerializer
from student.serializers import CourseSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from student.models import Enquiry
from datetime import datetime
from student.serializers import EnquirySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class EmployeeRegister(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        queryset = CustomUser.objects.all()
        serializer = UserSerializer(queryset,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status":200,"Message":"Emloyee has been added"})

class StudentRegister(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        queryset = CustomUser.objects.filter(is_student=True)
        serializer = StudentSerializer(queryset,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        id = request.data.get('id')
        course = request.data.get('course') or None
        standard = request.data.get('standard') or None
        school = request.data.get('school') or None
        contact = request.data.get('contact') or None
        address = request.data.get('address') or None
        pincode = request.data.get('pincode') or None
        nationality = request.data.get('nationality') or None
        stud = CustomUser.objects.filter(id=id).first()
        course_obj = Course.objects.get(id=course)
        stud.student_profile.course = course_obj
        stud.student_profile.standard = standard
        stud.student_profile.school = school
        stud.student_profile.contact = contact
        stud.student_profile.address = address
        stud.student_profile.pincode = pincode
        stud.student_profile.nationality = nationality
        stud.save()
        return Response({"status":200,"Message":"Student Profile has been created"})

class CourseRegister(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,pk=None,*args,**kwargs):
        if pk is not None:
            queryset = Course.objects.filter(id=pk).first()
            serializer = CourseSerializer(queryset)
            return Response(serializer.data)
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status":200,"Message":"Course has been added"})


class EnquiryManagement(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        enquiries = Enquiry.objects.filter()
        serializer = EnquirySerializer(enquiries,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer = EnquirySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status":200,"Message":"Enquiry has been added"})
    def patch(self,request,id=None,*args,**kwargs):
        id = self.kwargs["id"]
        if id is not None:
            enquiry_obj = Enquiry.objects.filter(id=id).first()
            print(enquiry_obj)
            enquiry_obj.under_review = True
            enquiry_obj.employee_handling = self.request.user
            enquiry_obj.resolved_at = datetime.now()
            enquiry_obj.save()
            return Response("Enquiry has been answered by ")
        return Response({"message":"Please enter user id"})
