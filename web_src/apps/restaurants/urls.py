from django.urls import re_path, include
from . import api

router = api.RestaurantRouter()
router.register('restaurant', api.RestaurantViewSet, base_name='restaurant')

restaurant_api = [
    re_path(r'^', include(router.urls))
]
