from django.urls import path
from .views import TopicView

urlpatterns = [
    path('content/', TopicView.as_view()),
]
