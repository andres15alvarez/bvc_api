from django.urls import path
from stockusd.views import StockUSDView


urlpatterns = [
	path('', StockUSDView.as_view())
]