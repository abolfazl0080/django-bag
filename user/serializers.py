from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import User


class RegisterSerialiser(serializers.Serializer):

    username = serializers.CharField(max_length= 80, min_length=6, allow_blank= False)
    email = serializers.EmailField(allow_blank= False)
    first_name = serializers.CharField(max_length=80, allow_blank= False)
    last_name = serializers.CharField(max_length=80, allow_blank= False)
    phone_number = serializers.CharField(max_length=11, min_length=11, allow_blank= False)
    password = serializers.CharField(max_length=30, min_length=6, allow_blank= False)
    password_confirm = serializers.CharField(max_length=30, min_length=6, allow_blank= False)

    def validate(self, attrs):
        if not (attrs['password'] == attrs['password_confirm']):
            raise ValidationError('رمز عبور با تایید رمز عبور برابر نیست')
        return super().validate(attrs)

    def create(self, vd:dict):
        new_user:User = User.objects.create(
            username = vd['username'],
            email =vd['email'],
            first_name =vd['first_name'],
            last_name =vd['last_name'],
            phone_number =vd['phone_number'],
        )
        new_user.set_password(vd['password'])
        new_user.save()
        return new_user
    