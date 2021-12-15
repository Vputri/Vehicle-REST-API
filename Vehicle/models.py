from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

class Vechicle_Brand(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Vechicle_Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    id_brand = models.ForeignKey(
        Vechicle_Brand, related_name="vechicle_brand", on_delete=models.CASCADE, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return '{} {}'.format(self.name, self.id_brand)

class Vechicle_Model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    id_type = models.ForeignKey(
        Vechicle_Type, related_name="vechicle_type", on_delete=models.CASCADE, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return '{} {}'.format(self.name, self.id_type)

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Vechicle_Year(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return str(self.year)

class Price_List(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    price = models.DecimalField(max_digits=18, decimal_places=0, default=0)
    id_model = models.ForeignKey(
        Vechicle_Model, related_name="vechiclemodel", on_delete=models.CASCADE, null=True
    )
    id_year = models.ForeignKey(
        Vechicle_Year, related_name="vechicle_year", on_delete=models.CASCADE, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {} {}'.format(str(self.price), str(self.id_year), self.id_model)