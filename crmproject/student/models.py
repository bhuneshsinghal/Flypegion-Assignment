from django.db import models
from user.models import CustomUser
from .choices import standardchoice
# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length=10,unique=True,null=True,blank=True)
    course_name = models.CharField(max_length=100,unique=True,null=True,blank=True)
    instructor = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='instructor',null=True) 
    def __str__(self):
        return self.course_name


class Student(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="student_profile",verbose_name="Student")
    standard = models.CharField(max_length=10,choices=standardchoice.choose)
    course = models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)    
    school = models.CharField(max_length=100,null=True,blank=True)
    contact = models.CharField(max_length=10,verbose_name="Mobile Number")
    address = models.CharField(max_length=100,null=True,blank=True)
    pincode = models.CharField(max_length=10,null=True,blank=True)
    nationality = models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return self.user.first_name


class Enquiry(models.Model):
    student_user = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="enquiry")
    description = models.TextField(max_length=500,null=True,blank=True)
    under_review = models.BooleanField(default=False)
    employee_handling = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="enquiry",null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
         verbose_name = "Enquiry"


   