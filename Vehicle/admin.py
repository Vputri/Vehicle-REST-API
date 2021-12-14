from django.contrib import admin
from .models import Vechicle_Brand, Vechicle_Type, Vechicle_Model, Vechicle_Year, Price_List

# Register your models here.
admin.site.register(Vechicle_Brand)
admin.site.register(Vechicle_Type)
admin.site.register(Vechicle_Model)
admin.site.register(Vechicle_Year)
admin.site.register(Price_List)
