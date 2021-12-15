from django.urls import path
from .views import *

urlpatterns = [
    path('api/brand/', Vechicle_BrandView.as_view()),
    path('api/brand/<int:id>', Vechicle_BrandView.as_view()),
    path('api/type/', Vechicle_TypeView.as_view()),
    path('api/type/<int:id>', Vechicle_TypeView.as_view()),
    path('api/model/', Vechicle_ModelView.as_view()),
    path('api/model/<int:id>', Vechicle_ModelView.as_view()),
    path('api/year/', Vechicle_YearView.as_view()),
    path('api/year/<int:id>', Vechicle_YearView.as_view()),
    path('api/pricelist/', Price_ListView.as_view()),
    path('api/pricelist/<int:id>', Price_ListView.as_view()),
    path('', home, name="home"),
]