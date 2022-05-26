from django.db import models

# Create your models here.

class home(models.Model):
    id=models.IntegerField(unique=True,primary_key=True)
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25,null=True)
    city=models.CharField(max_length=25)
    zipcode=models.IntegerField(max_length=6)

    class Meta:
        pass