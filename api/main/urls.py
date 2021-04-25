from .views import *
from django.urls import path


urlpatterns = [
    path('check-word/', Main.as_view()),
]