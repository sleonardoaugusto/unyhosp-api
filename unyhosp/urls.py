"""unyhosp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from unyhosp.core.api.hospital.view import HospitalViewSet
from unyhosp.core.api.uti.view import UTIViewSet
from unyhosp.core.api.pacient.view import PacientViewSet
from unyhosp.core.api.bed.view import BedViewSet
from unyhosp.core.api.attendance.view import AttendanceViewSet

router = routers.DefaultRouter()
router.register(r'hospitals', HospitalViewSet)
router.register(r'utis', UTIViewSet)
router.register(r'pacients', PacientViewSet)
router.register(r'beds', BedViewSet)
router.register(r'attendances', AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
