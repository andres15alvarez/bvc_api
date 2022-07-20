from django.urls import path
from stock.views import (
	StockView,
	MostTradedStockView
)


urlpatterns = [
	path('', StockView.as_view()),
	path('most_traded', MostTradedStockView.as_view())
]
