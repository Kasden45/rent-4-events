from django.contrib.auth.models import User, Group
from rest_framework import serializers

from Rent4Events.models import *
import django.contrib.auth.models as auth
from django.views.decorators.csrf import csrf_exempt
from django_restql.mixins import DynamicFieldsMixin


class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = auth.User
        fields = ['id', 'username', 'email', 'password', 'groups']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return auth.User.objects.create(**validated_data)

    def update(self, instance: auth.User, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance


class GroupSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = auth.Group
        fields = ['id', 'name']


class ProductSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['prodId', 'prodName', 'category', 'quantity', 'available', 'price', 'description', 'image']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)


class CategorySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = ['catId', 'catName', 'products']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Category.objects.create(**validated_data)


class OrderSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['orderId', 'client', 'startDate', 'endDate', 'address', 'totalCost', 'status']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Order.objects.create(**validated_data)


class ClientSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    # client_user = UserSerializer(many=False)
    class Meta:
        model = Client
        fields = ['userId', 'firstName', 'lastName', 'phoneNumber']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Client.objects.create(**validated_data)


class DriverSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['userId', 'firstName', 'lastName', 'birthDate', 'employmentDate', 'salary', 'phoneNumber']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Driver.objects.create(**validated_data)


class OrderPositionSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = OrderPosition
        fields = ['order', 'product', 'quantity']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return OrderPosition.objects.create(**validated_data)


class VehicleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['vehicleId', 'brand', 'model', 'year', 'licensePlate', 'carServiceTo', 'type', 'status']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Vehicle.objects.create(**validated_data)


class CourseSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['order', 'driver', 'vehicle', 'courseDate', 'type', 'status']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Course.objects.create(**validated_data)