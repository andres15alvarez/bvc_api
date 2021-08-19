from django.urls import path
from stockves.views import StockVESView


urlpatterns = [
	path('', StockVESView.as_view())
]