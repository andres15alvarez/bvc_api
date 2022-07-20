from django.urls import path
from exchange.views import ExchangeRateView


urlpatterns = [
	path('', ExchangeRateView.as_view()),
]
