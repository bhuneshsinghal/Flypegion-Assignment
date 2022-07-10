from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from student.models import Student
from rest_framework.authtoken.models import Token



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_student_profile(sender, instance=None, created=False, **kwargs):
    if created:
        if instance.is_student==True:
            instance.is_employee = False
            Student.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_student_profile(sender, instance=None, created=False, **kwargs):
    instance.student_profile.save()




@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)