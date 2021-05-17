import datetime

from django.db import models
from django.contrib.auth import models as m
import django.utils.timezone as timezone
# Create your models here.



class User(m.User):
    userId = models.BigAutoField(primary_key=True)

class Driver(models.Model):
    # driverId = models.BigAutoField(primary_key=True)
    userId = models.ForeignKey(
        User,
        primary_key=True,
        on_delete=models.CASCADE,
        verbose_name='DriverUser'
    )
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    birthDate = models.DateField()
    employmentDate = models.DateField(default=timezone.now())
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    phoneNumber = models.CharField(max_length=12, unique=True)


class Client(models.Model):
    # clientId = models.BigAutoField(primary_key=True)
    userId = models.ForeignKey(
        User,
        primary_key=True,
        on_delete=models.CASCADE,
        verbose_name='ClientUser'
    )
    firstName = models.CharField(max_length=30)  # nullable
    lastName = models.CharField(max_length=30)  # nullable
    phoneNumber = models.CharField(max_length=12, unique=True)  # nullable
    # address?


class Order(models.Model):
    STATUS_CHOICES = (
        ('OD', 'Odrzucone'),
        ('OC', 'Oczekujące'),
        ('DR', 'Do realizacji'),
        ('WT', 'W trakcie realizacji'),
        ('ZR', 'Zrealizowane'),
    )
    orderId = models.BigAutoField(primary_key=True)
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name="clientId",
    )
    startDate = models.DateField()
    endDate = models.DateField()
    address = models.CharField(max_length=80)
    totalCost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class Category(models.Model):
    catId = models.BigAutoField(primary_key=True)
    catName = models.CharField(max_length=50, unique=True)


class Product(models.Model):
    prodId = models.BigAutoField(primary_key=True)
    prodName = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="catId",
        to_field='catId',
        related_name='products'
    )
    quantity = models.PositiveIntegerField(default=1)
    available = models.PositiveIntegerField()  # <= quantity
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=500)  # nullable
    image = models.CharField(max_length=300, null=True)


class OrderPosition(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="orderId",

    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="productId"
    )
    quantity = models.PositiveIntegerField(default=1)


class Vehicle(models.Model):
    TYPE_CHOICE = (
        ('BU', 'Bus'),
        ('CI', 'Ciężarówka')
    )
    STATUS_CHOICE = (
        ('SP', 'Sprawny'),
        ('WW', 'W warsztacie'),
        ('NI', 'Niesprawny')
    )
    vehicleId = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=30) # nullable
    model = models.CharField(max_length=30) # nullable
    year = models.PositiveIntegerField() # nullable
    licensePlate = models.CharField(max_length=9, unique=True)
    carServiceTo = models.DateField() # nullable
    type = models.CharField(max_length=10, choices=TYPE_CHOICE) # nullable
    status = models.CharField(max_length=12, choices=STATUS_CHOICE) # nullable


class Course(models.Model):
    TYPE_CHOICES = (
        ('DO', 'Dostawa'),
        ('OD', 'Odbiór')
    )
    STATUS_CHOICES = (
        ('ZA', 'Zaplanowany'),
        ('WT', 'W trasie'),
        ('ZR', 'Zrealizowany')
    )
    courseId = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='orderId'
    )
    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        verbose_name='driverId'
    )
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        verbose_name='vehicleId'
    )
    courseDate = models.DateField()
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES) # Default = zaplanowany
