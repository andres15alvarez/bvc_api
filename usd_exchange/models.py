from django.db import models


class USDExchange(models.Model):

	# variation = models.DecimalField(max_digits=4, decimal_places=2)
	open = models.DecimalField(max_digits=12, decimal_places=2)
	close = models.DecimalField(max_digits=12, decimal_places=2)
	high = models.DecimalField(max_digits=12, decimal_places=2)
	low = models.DecimalField(max_digits=12, decimal_places=2)
	date = models.DateField()

	class Meta:
		db_table = 'usd_exchange'
		ordering = ['-date']
		verbose_name = 'usd exchange daily'

	def __str__(self):
		return f'O:{self.open} L:{self.low} H:{self.high} C:{self.close} at {self.date}'
