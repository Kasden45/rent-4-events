import decimal
import random

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django_filters import filters, rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from django_restql.mixins import QueryArgumentsMixin
from rest_framework.decorators import api_view, permission_classes, action

import django.contrib.auth.models as auth
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from Rent4Events.models import Product, OrderPosition
# from Rent4Events.serializers import UserSerializer, GroupSerializer, ProductSerializer
from Rent4Events.serializers import *
from functools import wraps
import jwt

from django.http import JsonResponse


def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]
    print(auth)
    return token


def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """

    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            print('decoded:', decoded)
            if decoded.get("permissions"):
                token_scopes = decoded["permissions"]
                for token_scope in token_scopes:
                    print('scope:', token_scope)
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response

        return decorated

    return require_scope


@api_view(['GET'])
@permission_classes([AllowAny])
def public(request):
    return JsonResponse({'message': 'Hello from a public endpoint! You don\'t need to be authenticated to see this.'})


@api_view(['GET'])
def private(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated to see this.'})


@api_view(['GET'])
@requires_scope('read:messages')
def private_scoped(request):
    return JsonResponse({
        'message': 'Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this.'})


"""
TESTING
"""


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = auth.User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = auth.Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]


class CustomSearchFilter(SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('name_only') == "1":
            return ['prodName']
        return super(CustomSearchFilter, self).get_search_fields(view, request)


class ProductViewSet(QueryArgumentsMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [OrderingFilter, DjangoFilterBackend, CustomSearchFilter]
    ordering_fields = ['prodName', 'price']
    search_fields = ['prodName', 'category__catName', 'description']

    def get_queryset(self):
        queryset = Product.objects.all()
        try:
            categories = eval(self.request.query_params.get('categories', []))
            print(categories)
            return queryset.filter(category__catId__in=categories)
        except TypeError:
            return queryset

    @action(methods=['get'], detail=True,
            url_path='similar', url_name='similar')
    def find_similar(self, request, pk=None):
        instance = self.get_object()
        # queryset = random.sample(Product.objects.filter(category_id=instance.category.catId), how_much)
        queryset = Product.objects.filter(~Q(prodId=instance.prodId), category_id=instance.category.catId).order_by(
            '?')[:5]
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            pass
        elif request.user.groups.filter(name='Klient'):
            request.data['userId'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DriverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows drivers to be viewed or edited.
    """
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [permissions.AllowAny]


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        print("request user", request.user)
        if request.user.is_staff:
            queryset = Order.objects.all()
        else:
            queryset = Order.objects.filter(client__userId__username=request.user.username)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            pass
        else:
            request.data['client'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        calculate_order_total(instance.orderId)
        return Response(serializer.data)


class VehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows vehicles to be viewed or edited.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.AllowAny]


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]


class MultipleFieldLookupMixin:
    def get_object(self):
        queryset = self.get_queryset()  # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        multi_filter = {field: self.kwargs[field] for field in self.lookup_fields}
        obj = get_object_or_404(queryset, **multi_filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj


def calculate_order_total(order_id):
    total = decimal.Decimal('0.0')
    order = Order.objects.get(orderId=order_id)
    date_diff = (order.endDate - order.startDate).days + 1
    for position in order.positions.all():
        total += decimal.Decimal(date_diff * position.quantity) * position.product.price
        print(total)

    order.totalCost = total
    order.save()


class OrderPositionViewSet(MultipleFieldLookupMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = OrderPosition.objects.all()
    # serializer_class = OrderPositionSerializer
    permission_classes = [permissions.AllowAny]
    lookup_fields = ['order_id', 'product_id']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ShowOrderPositionSerializer
        else:
            return OrderPositionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        calculate_order_total(serializer.validated_data['order'].orderId)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        calculate_order_total(instance.order_id)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        calculate_order_total(instance.order_id)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ImageViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows images to be viewed or edited.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.AllowAny]


def user_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def user_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


def group_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Group.objects.all()
        serializer = GroupSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# @api_view(['GET'])
# def public(request):
#     return HttpResponse("You don't need to be authenticated to see this")
#
#
# @api_view(['GET'])
# def private(request):
#     return HttpResponse("You should not see this message if not authenticated!")
