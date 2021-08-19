from django.db import models

from django.db import models

class StockVES(models.Model):

	code = models.CharField(max_length=5)
	open = models.DecimalField(max_digits=12, decimal_places=2)
	close = models.DecimalField(max_digits=12, decimal_places=2)
	high = models.DecimalField(max_digits=12, decimal_places=2)
	low = models.DecimalField(max_digits=12, decimal_places=2)
	date = models.DateField()

	class Meta:
		db_table = 'stock_ves'
		ordering = ['-date', 'code']
		verbose_name = 'stock ves daily'
		verbose_name_plural = 'stocks ves daily'
		constraints = [
			models.UniqueConstraint(fields=['code', 'date'],
				name='unique_code_date_ves')
		]

	def __str__(self):
		return f'{self.code} O:{self.open} L:{self.low} H:{self.high}'\
				f'C:{self.close} at {self.date}'
