"""dom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from ad.views import AdViewSet
from application.views import ApplicationViewSet
from meter.views import IndicationViewSet
from reservation.views import ReservationViewSet

router = SimpleRouter()

# router.register(r'meter', IndicationViewSet)
router.register(r'application', ApplicationViewSet)
router.register(r'ad', AdViewSet)
router.register(r'reservation', ReservationViewSet)
# router.register(r'registration', RegistrationViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]

