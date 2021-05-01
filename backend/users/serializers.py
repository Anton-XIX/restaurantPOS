from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import password_validation
from djoser.serializers import UserCreateSerializer

class CustomUserSerializer(UserCreateSerializer):
    # password = serializers.CharField(required=True, allow_blank=False, write_only=True)
    #
    # def create(self, validated_data):
    #     user = CustomUser(
    #         email=validated_data['email'], first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name'], is_waiter=validated_data['is_waiter'],
    #         phone_number=validated_data['phone_number'], is_cooker=validated_data['is_cooker'],
    #         is_staff=validated_data['is_staff'], is_admin=validated_data['is_admin']
    #     )
    #     if validated_data['is_admin']:
    #         user.is_waiter = False
    #         user.is_cooker = False
    #         user.role = 1
    #     elif validated_data['is_waiter']:
    #         user.is_cooker = False
    #         user.role = 2
    #     elif validated_data['is_cooker']:
    #         user.role = 3
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name', 'phone_number',
                  'is_admin', 'is_waiter', 'is_cooker',)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone_number',

                  )


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password1 = serializers.CharField(required=True, write_only=True)
    new_password2 = serializers.CharField(required=True, write_only=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Incorrect password')
        return value

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError('Password are not match')
        password_validation.validate_password(data['new_password1'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user
