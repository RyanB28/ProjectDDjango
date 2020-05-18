from django.urls import path
from .views import (
    viewrender)

urlpatterns = [
    path('/belangrijkeberichten', viewrender.as_view(), name='BelangrijkeBerichten-home')
]