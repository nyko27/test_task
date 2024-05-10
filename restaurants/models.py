from django.core.validators import MinLengthValidator
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(validators=[MinLengthValidator(5)])
    price = models.DecimalField(max_digits=8, decimal_places=2)


class DayOfWeek(models.TextChoices):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=DayOfWeek.choices)
    dishes = models.ManyToManyField(Dish)
