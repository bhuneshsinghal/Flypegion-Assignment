from django.contrib import admin

# Register your models here.
from .models import Course,Student,Enquiry

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_name', 'instructor')

admin.site.register(Course,CourseAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('standard','course','school')

admin.site.register(Student,StudentAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('description','under_review','employee_handling')

admin.site.register(Enquiry,EnquiryAdmin)

