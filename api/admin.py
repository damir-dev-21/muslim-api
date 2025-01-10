from django.contrib import admin
from .models import User,Point

# Register your models here.

@admin.register(User)
class Users(admin.ModelAdmin):
    fieldsets=(
        ('Информация о пользователе', {
            'fields': ('name', 'password', 'is_superuser')
        }),
    )
    list_display=('id','name')


@admin.register(Point)
class Points(admin.ModelAdmin):
    fieldsets=(
        ('Информация о точках', {
            'fields': ('title', 'latitude', 'longitude')
        }),
    )
    list_display=('id','title')