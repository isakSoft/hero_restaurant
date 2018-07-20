from rest_framework.response import Response
from rest_framework.routers import SimpleRouter, Route
from rest_framework import viewsets
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import Restaurant
from .serializers import RestaurantSerializer

UserModel = get_user_model()


class RestaurantRouter(SimpleRouter):
    """Simple API Router (read-only) for restaurant"""

    routes = [
        Route(
            url=r'^{prefix}/$',
            mapping={
                'get': 'list',
                'post': 'create',
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/$',
            mapping={
                'get': 'retrieve',
                'put': 'update',
                'delete': 'destroy'
            },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
    ]


class RestaurantViewSet(viewsets.ModelViewSet):
    """This class defines the behaviour of restaurant Api"""
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = ()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = RestaurantSerializer(queryset, many=True)
        return Response({'data': serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = RestaurantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'data': serializer.data})

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs['pk']
        restaurant = get_object_or_404(Restaurant, pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return Response({'data': serializer.data})

    def update(self, request, *args, **kwargs):
        pk = kwargs['pk']
        restaurant = get_object_or_404(Restaurant, pk=pk)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'data': serializer.data})

    def destroy(self, request, *args, **kwargs):
        pk = kwargs['pk']
        restaurant = get_object_or_404(Restaurant, pk=pk)
        self.perform_destroy(restaurant)
        return Response(status=status.HTTP_204_NO_CONTENT)