from rest_framework import serializers
from .models import Drinks, Category

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = ['id','category', 'name', 'description', 'created']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name', 'description', 'created']