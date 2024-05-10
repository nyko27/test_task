from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from restaurants.models import Menu, DayOfWeek


class EmployeeManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, password=None):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user


class Employee(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=120)
    password = models.CharField(max_length=128)

    objects = EmployeeManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']


class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING)
    day_of_week = models.CharField(max_length=9, choices=DayOfWeek.choices)
