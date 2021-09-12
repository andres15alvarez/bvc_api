from django.urls import path
from ibc.views import IBCView


urlpatterns = [
	path('', IBCView.as_view()),
]