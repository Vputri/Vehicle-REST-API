from django.urls import path
from .views import *

urlpatterns = [
    path('brand/', Vechicle_BrandView.as_view()),
    path('brand/<int:id>', Vechicle_BrandView.as_view()),
    path('type/', Vechicle_TypeView.as_view()),
    path('type/<int:id>', Vechicle_TypeView.as_view()),
    path('model/', Vechicle_ModelView.as_view()),
    path('model/<int:id>', Vechicle_ModelView.as_view()),
    path('year/', Vechicle_YearView.as_view()),
    path('year/<int:id>', Vechicle_YearView.as_view()),
    path('pricelist/', Price_ListView.as_view()),
    path('pricelist/<int:id>', Price_ListView.as_view()),
]