from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet

router = DefaultRouter()
router.register('tables', BookingViewSet, basename='booking')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Homepage
    path('restaurant/', include('restaurant.urls')),

    # Menu API
    path('restaurant/menu/', include('restaurant.menu_urls')),

    # Booking API
    path('restaurant/booking/', include(router.urls)),

    # Djoser authentication
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]