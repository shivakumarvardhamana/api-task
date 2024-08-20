from django.shortcuts import render


from .serializer import userserializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import user
from .serializer import userserializer

@api_view(['GET'])
def get(request):
    persons = user.objects.all()
    serializer = userserializer(persons, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = userserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
