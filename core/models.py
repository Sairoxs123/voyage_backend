from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    name = models.CharField("Name", max_length=50)
    email = models.EmailField("Email")
    password = models.CharField("Password", max_length=50)
    dob = models.DateField("Date of Birth")
