from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Users

class UsersAdminForm(admin.ModelAdmin):
    """admin管理ページフォーム情報"""
    fieldsets = [
        (None,{'fields':['icon','username',]}),
        ("userinfo",{'fields':[
            "password",
            "last_login",
            "is_superuser",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
            ]})
    ]
admin.site.register(Users,  UsersAdminForm)
