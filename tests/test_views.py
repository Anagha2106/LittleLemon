
from rest_framework.test import APITestCase
from rest_framework import status

from restaurant.models import MenuItem


class MenuViewTest(APITestCase):

    def setUp(self):
        MenuItem.objects.create(
            title="Pizza",
            price=150,
            inventory=10
        )

        MenuItem.objects.create(
            title="Pasta",
            price=120,
            inventory=15
        )

    def test_getall(self):
        response = self.client.get(
            '/restaurant/menu/items/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(len(response.data), 2)

        self.assertEqual(
            response.data[0]['title'],
            'Pizza'
        )

    def test_create_menu_item(self):
        data = {
            'title': 'Burger',
            'price': '100.00',
            'inventory': 20
        }

        response = self.client.post(
            '/restaurant/menu/items/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            MenuItem.objects.count(),
            3
        )
