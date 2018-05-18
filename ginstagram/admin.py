from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Users

class UsersAdmin2(admin.ModelAdmin):
    fieldsets = [
            (None,{'fields':['icon']})
            ]
admin.site.register(Users,  UsersAdmin2)
