from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class RegisterUser(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100,default="")
    last_name = models.CharField(max_length=100, default="")
    email=models.CharField(max_length=255,default="")
    password=models.CharField(max_length=200,default="")
    phone=models.IntegerField(default="")
    gender=models.CharField(max_length=255,default="")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class ToDoList(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.AutoField(primary_key=True)
    date=models.CharField(max_length=255,default="")
    done=models.BooleanField(default=False)
    todo=models.CharField(max_length=255,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
