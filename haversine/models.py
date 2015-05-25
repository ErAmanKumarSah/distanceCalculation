from django.db import models

# Create your models here.

class Area(models.Model):
	locality_id = models.IntegerField(blank=False)
	locality_name = models.CharField(max_length=40)
	city = models.CharField(max_length=30)
	latitude = models.DecimalField(max_digits=11, decimal_places=8)
	longitude = models.DecimalField(max_digits=11, decimal_places=8)
	added_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.locality_name



