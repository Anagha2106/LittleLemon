from django.test import TestCase
from restaurant.models import Menu, Booking


class MenuTest(TestCase):

    def test_get_item(self):
        item = Menu.objects.create(
            title="IceCream",
            price=80,
            inventory=100
        )

        self.assertEqual(str(item), "IceCream : 80.00")


class BookingTest(TestCase):

    def test_get_booking(self):
        booking = Booking.objects.create(
            name="Anagha",
            no_of_guests=3,
            booking_date="2026-11-15"
        )

        self.assertEqual(
            str(booking),
            "Anagha - 2026-11-15"
        )