from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from .models import Restaurant
import datetime


class ModelTestCase(TestCase):
    """This class has test suite for restaurant model"""

    def setUp(self):
        """Define variables and test client model"""
        self.restaurant_name = 'Hero Restaurant'
        self.restaurant = Restaurant(name=self.restaurant_name)

    def test_can_create_new_restaurant(self):
        """Test restaurant model to create new restaurant"""
        no_restaurant = Restaurant.objects.count()
        self.restaurant.save()
        new_restaurant = Restaurant.objects.count()
        self.assertEqual(new_restaurant, 1)
        self.assertNotEqual(no_restaurant, new_restaurant)

    def test_can_change_restaurant_name(self):
        old_restaurant_name = self.restaurant_name
        self.restaurant.save()
        new_restaurant_name = 'New Hero Restaurant'
        self.restaurant = Restaurant(name=new_restaurant_name)
        self.restaurant.save()
        self.assertNotEqual(old_restaurant_name, self.restaurant.name)

    def test_can_delete_restaurant(self):
        self.restaurant.save()
        before_del_count = Restaurant.objects.count()
        self.restaurant.delete()
        after_del_count = Restaurant.objects.count()
        self.assertNotEqual(before_del_count, after_del_count)


class ViewTestCase(APITestCase):
    """This class has test suite for API Views"""

    def setUp(self):
        self.restaurant_data = {
            'name': 'Berlin Hero Restaurant',
            'opens_at': datetime.time(10, 00),
            'closes_at': datetime.time(21, 00)
        }
        self.response = self.client.post(
            reverse('restaurant-list'),
            self.restaurant_data,
            format='json'
        )

    def test_can_create_restaurant(self):
        """Test api create restaurant ability"""
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        data = self.response.data['data']
        self.assertEqual(data['name'], self.restaurant_data['name'])

    def test_can_retrieve_restaurant(self):
        """Test api can retrieve restaurant"""
        restaurant = Restaurant.objects.get()
        response = self.client.get(
            reverse('restaurant-detail',
                    kwargs={'pk': restaurant.id}
                    ),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, restaurant)
        data = self.response.data['data']
        self.assertEqual(data['name'], restaurant.name)

    def test_can_update_restaurant(self):
        """Test api can update restaurant"""
        restaurant = Restaurant.objects.get()
        new_restaurant = {
            'name': 'Berlin Restaurant 2 updated'
        }
        response = self.client.put(
            reverse('restaurant-detail',
                    kwargs={'pk': restaurant.id}
                    ),
            new_restaurant,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, new_restaurant['name'])

    def test_can_destroy_restaurant(self):
        """Test api can destroy restaurant"""
        restaurant = Restaurant.objects.get()
        response = self.client.delete(
            reverse('restaurant-detail',
                    kwargs={'pk': restaurant.id}
                    ),
            format='json'
        )
        restaurant_qs = Restaurant.objects.filter(pk=restaurant.id)
        self.assertFalse(restaurant_qs)
