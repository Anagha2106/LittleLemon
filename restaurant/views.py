
from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer


# Home page
def index(request):
    return render(request, 'index.html')


# Display and create menu items
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


# Retrieve, update and delete a menu item
class SingleMenuItemView(
    generics.RetrieveUpdateAPIView,
    generics.DestroyAPIView
):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


# Table booking API
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
