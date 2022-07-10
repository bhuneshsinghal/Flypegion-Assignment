from user.models import CustomUser
def verify_token(auth_token):
    try:
        user = CustomUser.objects.filter(auth_token=auth_token).first()
        if user:
            user.is_verified = True
            user.save()
    except Exception as e:
        print(e)