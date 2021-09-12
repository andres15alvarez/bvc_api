from django.urls import path
from usd_exchange.views import USDExchangeView 


urlpatterns = [
	path('', USDExchangeView.as_view()),
]