from django.urls import path
from .views import Price_ListView

urlpatterns = [
    path('pricelist/', Price_ListView.as_view()),
]