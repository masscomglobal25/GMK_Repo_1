from rest_framework import serializers
from app_login.models import Login, UserTokenRegister


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('SortId',
                  'LoginId',
                  'UserId',
                  'UserType',
                  'EmailId',
                  'Password',
                  'Token',
                  'Status')


class LoginSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = (
            # 'SortId',
            'LoginId',
            'UserId',
            'UserType',
            'EmailId',
            'Password',
            'Status')


class LoginUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = (
            # 'SortId',
            'LoginId',
            'UserId',
            'UserType',
            'EmailId',
            'Password',)


class LoginStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = (
            # 'SortId',
            'UserId',
            'UserType',
            'Status')


class LoginAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = (
            'SortId',
            'LoginId',
            'UserId',
            'UserType',
            'EmailId',
            'Token',
            'Status')


class SocialLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = (
            'SortId',
            'LoginId',
            'UserId',
            'UserType',
            'EmailId',
            'Status')


class UserTokenRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTokenRegister
        fields = (
            'TokenId',
            'LoginId',
            'EmailId',
            'UserType',
            'LoginType')
