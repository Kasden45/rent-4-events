from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from Rent4Events.models import *
import django.contrib.auth.models as auth
from django.views.decorators.csrf import csrf_exempt
from django_restql.mixins import DynamicFieldsMixin
from django.db import IntegrityError


class GroupSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = auth.Group
        fields = ['id', 'name']


class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = auth.User
        fields = ['id', 'username', 'email', 'password', 'groups', 'is_active']
        read_only_fields = ['is_active', 'is_staff']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        new_user = auth.User(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],

        )

        new_user.set_password(new_user.password)
        new_user.save()

        for group in validated_data['groups']:
            my_group = Group.objects.get(name=group)
            new_user.groups.add(my_group)
            new_user.save()
        # my_group.user_set.add(new_user)
        # my_group.save()
        return new_user

    def update(self, instance: auth.User, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        groups = instance.groups
        for group in groups.all():
            instance.groups.remove(group)
        for group in validated_data['groups']:
            my_group = Group.objects.get(name=group)
            instance.groups.add(my_group)
            instance.save()
        instance.save()
        return instance



class ImageSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['imageId', 'imageName', 'imageUrl', 'product']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Image.objects.create(**validated_data)


class ProductSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    images = ImageSerializer(many=True, allow_null=True, required=False)

    class Meta:
        model = Product
        fields = ['prodId', 'prodName', 'category', 'quantity', 'available', 'price', 'description', 'images']
        read_only_fields = ['images']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        # return Product.objects.create(**validated_data)constraint_available_lte_quantity
        try:
            return Product.objects.create(**validated_data)
        except IntegrityError as e:
            print(e.__str__())
            if 'CHECK constraint' in e.__str__():
                additional_info = ""
                if 'constraint_available_lte_quantity' in e.__str__():
                    additional_info = "'Available' can't be greater than 'Quantity'!"
                elif 'quantity' in e.__str__():
                    additional_info = "'Quantity' must be greater than or equal 0!"
                elif 'available' in e.__str__():
                    additional_info = "'Available' must be greater than or equal 0!"
                elif 'constraint_price_greater_than_zero' in e.__str__():
                    additional_info = "'Price' must be greater than or equal 0! "
                raise serializers.ValidationError("{} - {}".format(e.__cause__, additional_info))


class CategorySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    products = ProductSerializer(many=True, allow_null=True, required=False)

    class Meta:
        model = Category
        fields = ['catId', 'catName', 'products']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Category.objects.create(**validated_data)


class OrderPositionSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = OrderPosition
        fields = ['order', 'product', 'quantity']


class ShowOrderPositionSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    product = ProductSerializer(many=False, allow_null=True, required=False)

    class Meta:
        model = OrderPosition
        fields = ['order', 'product', 'quantity']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        try:
            return OrderPosition.objects.create(**validated_data)
        except IntegrityError as e:
            print(e.__str__())
            if 'UNIQUE constraint' in e.__str__():
                print("UNIQUE!")
                raise serializers.ValidationError(e.__cause__)
            else:
                raise serializers.ValidationError(e.__cause__)

class OrderSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    positions = ShowOrderPositionSerializer(many=True, allow_null=True, required=False)

    class Meta:
        model = Order
        fields = ['orderId', 'client', 'startDate', 'endDate', 'address', 'isTransport', 'totalCost', 'status', 'creationDate', 'comment', 'positions']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        _client = validated_data.get('client', Order.client)
        _status = validated_data.get('status', Order.status)
        if _status == "Robocze":
            count = len(Order.objects.filter(models.Q(client=_client), models.Q(status="Robocze")))
            if count >= 1:
                raise serializers.ValidationError("This client already has order with status 'Robocze'!")
        try:
            return Order.objects.create(**validated_data)
        except IntegrityError as e:
            print(e.__str__())
            if 'constraint_start_end' in e.__str__():
                print("e.__cause__")
                raise serializers.ValidationError("End date can't appear before start date!")
            elif 'constraint_totalCost_greater_than_zero' in e.__str__():
                raise serializers.ValidationError("Total cost must be greater than 0!")


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
        read_only_fields = ['userId']
        return Driver.objects.create(**validated_data)


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
