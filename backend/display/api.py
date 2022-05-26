from rest_framework import viewsets,permissions

from . import serializers
from . import models


class home(viewsets.ModelViewSet):
    queryset = models.home.objects.all()
    serializer_class = serializers.home

