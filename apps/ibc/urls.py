from django.urls import path
from apps.ibc.views import IBCView


urlpatterns = [
	path('', IBCView.as_view()),
]
