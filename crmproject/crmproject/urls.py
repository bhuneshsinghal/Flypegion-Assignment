"""crmproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views
from rest_framework.authtoken import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/view/', views.EmployeeRegister.as_view() , name="user_view"),
    path('user/student/view/',views.StudentRegister.as_view(),name='student_view'),
    path('user/course/',views.CourseRegister.as_view(),name="course_view"),
    path('employee/enquiry/view/',views.EnquiryManagement.as_view(),name="enquiry"),
    path('employee/enquiry/view/<int:id>/',views.EnquiryManagement.as_view(),name="enquiry_with_id"),
    path('api-token-auth/',v.obtain_auth_token,name="token_generate_url"),
]   
