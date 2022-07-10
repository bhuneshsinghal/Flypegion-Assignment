from rest_framework import serializers
from student.serializers import StudentSerializer
from .models import CustomUser
from django.utils.translation import gettext_lazy as _
import re


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'},write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    date_of_birth = serializers.DateField()
    gender = serializers.CharField()
    is_employee = serializers.BooleanField()
    is_student = serializers.BooleanField()


    def validate(self,data):
        password = data['password']
        special_char = '[@_!#$%^&*()<>?/\|}{~:]'
        regex = re.compile(special_char)
        digit_count = 0
        alphabet_count = 0
        if(regex.search(password) == None):
            raise serializers.ValidationError(_("Password should contain atleast 2 Special Character"))
        else:
            special_count = 0
            for i in password:
                if i.isdigit():
                    digit_count+=1
                if i.isalpha():
                    alphabet_count+=1
                if i in special_char:
                    special_count+=1
            if alphabet_count<8:
                raise serializers.ValidationError(_("Password should contain 8 alphabets"))
            if digit_count<2:
                raise serializers.ValidationError(_("Password should contain atleast 2 digit"))
            if special_count<2:
                raise serializers.ValidationError(_("Password should contain atleast 2 Special Character"))
        return data

    def create(self,validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
    

        

class StudentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(source="student_profile")
    class Meta:
        model = CustomUser
        fields = ['id','email','first_name','last_name','student']