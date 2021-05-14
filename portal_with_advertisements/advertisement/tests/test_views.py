import datetime
import json
from decimal import Decimal
from unittest import TestCase

from django.urls import reverse
from rest_framework import status

from advertisement.models import Category, Offer
from advertisement.serializers import CategorySerializer, OffersListSerializer, OfferDetailSerializer
from advertisement.tests.factories import CategoryFactory, OfferFactory
from rest_framework.test import APITestCase



class CategoryTestCase(APITestCase):
    def setUp(self) -> None:
        self.car = CategoryFactory(name="Car", ordering=False)
        self.boat = CategoryFactory(name="Boat", ordering=True)

    def test_category_list(self):
        response = self.client.get('/api/category/')
        serializer_data = CategorySerializer([self.boat, self.car], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_category_detail(self):
        response = self.client.get(f'/api/category/{self.car.id}')
        serializer_data = CategorySerializer(self.car).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_category_create(self):
        data = {
            "name": "test",
            "ordering": "false"
        }
        json_data = json.dumps(data)
        response = self.client.post('/api/category/', data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, Category.objects.all().count())

    def test_category_update(self):
        data = {
            "id": self.car.id,
            "name": "Test",
            "ordering": "true"
        }
        json_data = json.dumps(data)
        response = self.client.put(f'/api/category/{self.car.id}', json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.car.refresh_from_db()
        self.assertEqual("Test", self.car.name)
        self.assertTrue(self.car.ordering)

    def test_category_delete(self):
        response = self.client.delete(f'/api/category/{self.car.id}')
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(1, Category.objects.all().count())


class OfferTestCase(APITestCase):
    def setUp(self) -> None:
        self.offer_1 = OfferFactory(category__name="car", title="BMW", description="M6", price=250000.25,
                                    created_at=datetime.datetime.now())
        self.offer_2 = OfferFactory(category__name="boat", title="Yamaha", price=53799.25,
                                    created_at=datetime.datetime.now())

    def test_offer_list(self):
        response = self.client.get('/api/offers/')
        serializer_data = OffersListSerializer([self.offer_1, self.offer_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_offer_detail(self):
        response = self.client.get(f'/api/offers/{self.offer_1.id}')
        serializer_data = OfferDetailSerializer(self.offer_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_offer_create(self):
        data = {
            "title": "Test",
            "description": "Lorem ipsum",
            "price": "1000.00",
            "created_at": "2021-05-10 13:49:09.713743+0000",
            "category": 1
        }
        json_data = json.dumps(data)
        response = self.client.post('/api/offers/', data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, Offer.objects.all().count())

    #
    def test_offer_update(self):
        data = {
                "id": self.offer_1.id,
                "title": "Test",
                "description": "Lorem ipsum",
                "price": "50.00",
                "created_at": "2021-05-10 13:49:09.713743+0000",
                "category": self.offer_1.category.id
        }
        json_data = json.dumps(data)
        response = self.client.put(f'/api/offers/{self.offer_1.id}', json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.offer_1.refresh_from_db()
        self.assertEqual("Test", self.offer_1.title)
        self.assertEqual(Decimal(50.00), self.offer_1.price)

    def test_category_delete(self):
        response = self.client.delete(f'/api/category/{self.offer_1.id}')
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(1, Offer.objects.all().count())
