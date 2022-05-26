from django.http import JsonResponse
from django.shortcuts import render

#views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers

@api_view(['get'])
def printdata(request):
    homeservice=serializers.homeservice
    serializer = homeservice.get_all_details()
    print("data",serializer.data)
    return JsonResponse({serializer.data})