from rest_framework import serializers
from . import models

class home(serializers.ModelSerializer):
    class Meta:
        model=models.home
        fields=[
            "id",
            "first_name",
            "last_name",
            "city",
            "zipcode"
        ]

class homeservice:
    @classmethod
    def get_all_details(cls):
        names_obj=models.home.objects. \
            all.values(
            "id",
            "first_name",
            "last_name",
            "city",
            "zipcode",
        )[0]
        return names_obj