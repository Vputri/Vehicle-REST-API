from django.urls import path
from .views import Price_ListView, home

urlpatterns = [
    path('pricelist/', Price_ListView.as_view()),
    path('', home, name="home"),
]