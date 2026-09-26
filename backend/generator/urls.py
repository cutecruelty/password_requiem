from django.urls import path
from .views import GenerateView, PolicyListCreateView

urlpatterns = [
    path('generate/', GenerateView.as_view()),
    path('policies/', PolicyListCreateView.as_view()),
]