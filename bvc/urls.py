"""bvc URL Configuration"""
from django.urls import path, include

urlpatterns = [
    path('stock/', include('stock.urls')),
    path('exchange/', include('exchange.urls')),
    path('ibc/', include('ibc.urls'))
]
