from django.http import JsonResponse
from .models import Drinks
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def jls_extract_def(status):
    return status


@api_view(['GET', 'POST'])    
def drink_list(request):
    if request.method == 'GET':
        drinks = Drinks.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse({'drinks' : serializer.data})

    if request.method == 'POST':
        serializer = DrinkSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):
    try:
        drink = Drinks.objects.get(id = id)
    except Drinks.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)

    if request.method == 'DELETE':
        drink.delete()