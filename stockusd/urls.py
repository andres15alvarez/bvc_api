from django.urls import path
from stockusd.views import (
	StockUSDView,
	MostTradedStockUSDView
)


urlpatterns = [
	path('', StockUSDView.as_view()),
	path('most_traded', MostTradedStockUSDView.as_view())
]