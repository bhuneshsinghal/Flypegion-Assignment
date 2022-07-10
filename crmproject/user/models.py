from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from .choices import genderchoice



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50,null=True,blank=True,verbose_name="First Name")
    last_name = models.CharField(max_length=50,null=True,blank=True,verbose_name="Last Name")
    date_of_birth = models.DateField(null=True,blank=True,verbose_name="Birth Date")
    gender = models.CharField(max_length=20,choices=genderchoice.choose,default='Male',verbose_name='Gender')
    verify_token = models.CharField(max_length=200,null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now,verbose_name="Joining Date")
    is_employee = models.BooleanField(default=True,verbose_name='Employee')
    is_student = models.BooleanField(default=False,verbose_name="Student")
   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

