from wsgiref.validate import validator
from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User

def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError("admin cannot be in email")
    

# With Model Serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'validators': (clean_email,)}
        }

    def validate_username(self, value):
        if value == 'admin':
            raise serializers.ValidationError("username cannot be admin")
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("passwords must match")
        return data

    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)


# class UserRegisterSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     email = serializers.EmailField(required=True, validator=[clean_email])
#     password = serializers.CharField(required=True, write_only=True)
#     password2 = serializers.CharField(required=True, write_only=True)

#     def validate_username(self, value):
#         if value == 'admin':
#             raise serializers.ValidationError("username cannot be admin")
#         return value

#     def validate(self, data):
#         if data['password'] != data['password2']:
#             raise serializers.ValidationError("passwords must match")
#         return data