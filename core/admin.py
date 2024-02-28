from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Users)

class UsersAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email"]
    ordering = ["id"]
    search_fields  = ["name", "username", "email"]
