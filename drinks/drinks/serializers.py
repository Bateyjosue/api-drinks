from rest_framework import serializers
from .models import Drinks, Category


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = ['id', 'category', 'name', 'description', 'created']

    def validate_drink_name(self, drink_name):
        if Drinks.objects.filter(drink=drink_name).exists():
            raise serializers.ValidationError('Drink Already exists')
        return drink_name


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created']

    def validate_category_name(self, value):
        if Category.objects.filter(name = value).exists():
            raise serializers.ValidationError('Category already exists')
        return value