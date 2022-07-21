"""bvc URL Configuration"""
from django.urls import path, include

urlpatterns = [
    path('stock', include('apps.stock.urls')),
    path('exchange', include('apps.exchange.urls')),
    path('ibc', include('apps.ibc.urls'))
]
