from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin



class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser, PermissionsMixin):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    name = models.CharField(unique=True, max_length=100,
                            verbose_name="Name")
    password = models.CharField(
        max_length=100, verbose_name="Password") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)

    # USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['name',"password"]

    def __str__(self):
        return self.name
    

class Point(TimeBasedModel):

    class Meta:
        verbose_name = 'Point'
        verbose_name_plural = 'Points'    

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,default="")
    latitude = models.CharField(
        max_length=255, verbose_name="Latitude", blank=True)
    longitude = models.CharField(
        max_length=255, verbose_name="Longitude", blank=True)    