from django.db import models

class CountryGDP(models.Model):
	name = models.CharField(max_length=50)
	code = models.CharField(max_length=5)
	year = models.CharField(max_length=4)
	value = models.DecimalField(default=0.00,max_digits=1000,decimal_places=2)

	def __str__(self):
		return self.name