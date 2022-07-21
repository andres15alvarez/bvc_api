from django.urls import path
from apps.exchange.views import ExchangeRateView


urlpatterns = [
	path('', ExchangeRateView.as_view()),
]
