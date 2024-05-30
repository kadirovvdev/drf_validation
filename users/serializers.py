import validators
from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'



    def validate(self, data):
        if data['username'].isalnum():
            return data

        raise serializers.ValidationError({'username': 'Name must be alphanumeric'})

    def validate_first_name(self, data):

        if any(i.isdigit() for i in data):
            raise serializers.ValidationError("First Name maydonida raqam bo'lmasligi kerak")
        return data

    def validate_last_name(self, data):

        if any(i.isdigit() for i in data):
            raise serializers.ValidationError("Last Name maydonida raqam bo'lmasligi kerak")
        return data

    def validate_email(self, data):
        if validators.email(data):
            return data
        raise serializers.ValidationError("Email not valid")


    def validate_phone(self, data):
        if data.startswith("+998") and len(data) < 14:
            return data
        raise serializers.ValidationError("Phone not valid")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'