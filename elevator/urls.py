from django.urls import path
from .views import ElevatorView

urlpatterns = [
    path('get_or_create/', ElevatorView.as_view()),
]