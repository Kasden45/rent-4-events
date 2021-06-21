import datetime
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db import models
from django.contrib.auth import models as m
import django.utils.timezone as timezones
from datetime import datetime
# Create your models here.
from django.db.models import UniqueConstraint

import Rent4Events


class User(m.User):
    userId = models.BigAutoField(primary_key=True)


class Driver(models.Model):
    # driverId = models.BigAutoField(primary_key=True)
    userId = models.OneToOneField(
        m.User,
        primary_key=True,
        to_field='id',
        on_delete=models.CASCADE,
        verbose_name='DriverUser'
    )
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    birthDate = models.DateField()
    employmentDate = models.DateField(default=timezones.now)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    phoneNumber = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return f'{self.userId} {self.firstName} {self.lastName} {self.birthDate}'


class Client(models.Model):
    # clientId = models.BigAutoField(primary_key=True)
    userId = models.OneToOneField(
        m.User,
        primary_key=True,
        to_field='id',
        on_delete=models.CASCADE,
        verbose_name='ClientUser'
    )
    firstName = models.CharField(max_length=30, blank=True, null=True)  # nullable
    lastName = models.CharField(max_length=30, blank=True, null=True)  # nullable
    phoneNumber = models.CharField(max_length=12, unique=True, blank=True, null=True)  # nullable

    # address?

    def __str__(self):
        return f'{self.userId} {self.firstName} {self.lastName} {self.phoneNumber}'


class Order(models.Model):
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(startDate__lte=models.F("endDate")), name='constraint_start_end'),
            models.CheckConstraint(check=models.Q(totalCost__gte=0.0),
                                   name='constraint_totalCost_greater_than_zero'),
        ]

    STATUS_CHOICES = (
        ('Odrzucone', 'Odrzucone'),
        ('Oczekujące', 'Oczekujące'),
        ('Do realizacji', 'Do realizacji'),
        ('W trakcie negocjacji', 'W trakcie negocjacji'),
        ('W trakcie realizacji', 'W trakcie realizacji'),
        ('Zrealizowane', 'Zrealizowane'),
        ('Robocze', 'Robocze'),
        ('Anulowane', 'Anulowane'),
        ('Edytowane', 'Edytowane')
    )
    orderId = models.BigAutoField(primary_key=True)
    client = models.ForeignKey(
        Client,
        to_field='userId',
        on_delete=models.CASCADE,
        verbose_name="clientId"
    )
    creationDate = models.DateField(default=timezones.now)
    startDate = models.DateField()
    endDate = models.DateField()
    address = models.CharField(max_length=80)
    isTransport = models.BooleanField(default=False)
    isEdited = models.BooleanField(default=False)
    totalCost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    comment = models.CharField(max_length=1000, blank=True, null=True)


class Category(models.Model):
    catId = models.BigAutoField(primary_key=True)
    catName = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.catName


class Product(models.Model):
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(available__lte=models.F("quantity")),
                                   name='constraint_available_lte_quantity'),
            models.CheckConstraint(check=models.Q(price__gte=0.0),
                                   name='constraint_price_greater_than_zero'),
        ]

    prodId = models.BigAutoField(primary_key=True)
    prodName = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="catId",
        to_field='catId',
        related_name='products'
    )
    quantity = models.PositiveIntegerField(default=1, error_messages={
        'check': "Quantity must be positive!"
    })
    available = models.PositiveIntegerField()  # <= quantity
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=500, blank=True, null=True)  # nullable
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.prodName


class OrderPosition(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['order_id', 'product_id'], name='constraint_PK_OrderPosition'),
        ]

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        to_field='orderId',
        verbose_name="orderId",
        related_name='positions',

    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        to_field='prodId',
        verbose_name="productId"
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.order.client.firstName} {self.order.client.lastName} : {self.product.prodName} : {self.quantity}'


class Vehicle(models.Model):
    TYPE_CHOICE = (
        ('Bus', 'Bus'),
        ('Ciężarówka', 'Ciężarówka')
    )
    STATUS_CHOICE = (
        ('Sprawny', 'Sprawny'),
        ('W warsztacie', 'W warsztacie'),
        ('Niesprawny', 'Niesprawny')
    )
    vehicleId = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=30, blank=True, null=True)  # nullable
    model = models.CharField(max_length=30, blank=True, null=True)  # nullable
    year = models.PositiveIntegerField(blank=True, null=True)  # nullable
    licensePlate = models.CharField(max_length=9, unique=True)
    carServiceTo = models.DateField(blank=True, null=True)  # nullable
    type = models.CharField(max_length=10, choices=TYPE_CHOICE, blank=True, null=True)  # nullable
    status = models.CharField(max_length=12, choices=STATUS_CHOICE, blank=True, null=True)  # nullable

    def __str__(self):
        return f'{self.brand} {self.model} {self.year} {self.licensePlate}'


class Course(models.Model):
    TYPE_CHOICES = (
        ('Dostawa', 'Dostawa'),
        ('Odbiór', 'Odbiór')
    )
    STATUS_CHOICES = (
        ('Zaplanowany', 'Zaplanowany'),
        ('W trasie', 'W trasie'),
        ('Zrealizowany', 'Zrealizowany')
    )
    courseId = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        to_field='orderId',
        verbose_name='orderId'
    )
    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        to_field='userId',
        verbose_name='driverId'
    )
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        to_field='vehicleId',
        verbose_name='vehicleId'
    )
    courseDate = models.DateField()
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Zaplanowany')  # Default = zaplanowany

    def __str__(self):
        return f'{self.courseId} Driver: {self.driver.firstName} {self.driver.lastName} ' \
               f'Client: {self.order.client.firstName} {self.order.client.lastName} Date: {self.courseDate}' \
               f' Status: {self.status}'


def user_directory_path(instance, filename):
    print(instance)
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f ")
    return 'uploads/{}/{}/{}-{}'.format(instance.product.category.catName, instance.product.prodName, date, filename)


class Image(models.Model):
    imageId = models.BigAutoField(primary_key=True)
    imageName = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="prodId",
        to_field='prodId',
        related_name='images',
        null=True
    )
    imageField = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
