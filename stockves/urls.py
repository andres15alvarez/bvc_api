from django.urls import path
from stockves.views import (
	StockVESView,
	MostTradedStockVESView
) 


urlpatterns = [
	path('', StockVESView.as_view()),
	path('most_traded', MostTradedStockVESView.as_view())
]