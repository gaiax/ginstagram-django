from django.contrib import admin
from .models import User


class UserAdminForm(admin.ModelAdmin):
    """admin管理ページフォーム情報"""
    fieldsets = [
        (None, {'fields': ['icon', 'username']}),
        ("userinfo", {'fields': [
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


admin.site.register(User,  UserAdminForm)
