from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.object.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class Vechicle_BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vechicle_Brand
        fields = '__all__'

class Vechicle_TypeSerializer(serializers.ModelSerializer):
    id_brand = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Vechicle_Type
        fields = ['id','name', 'id_brand', 'created_at', 'updated_at']

class Vechicle_ModelSerializer(serializers.ModelSerializer):
    id_type = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Vechicle_Model
        fields = ['id','name', 'id_type', 'created_at', 'updated_at']

class Vechicle_YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vechicle_Year
        fields = '__all__'

class Price_ListSerializer(serializers.ModelSerializer):
    id_model = serializers.PrimaryKeyRelatedField(read_only=True)
    id_year = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Price_List
        fields = ['id','code', 'price', 'id_model', 'id_year', 'created_at', 'updated_at']