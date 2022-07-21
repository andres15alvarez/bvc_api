from django.db import models

class Stock(models.Model):

	code = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name="stocks")
	volume = models.PositiveIntegerField()
	variation = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
	open = models.DecimalField(max_digits=12, decimal_places=2)
	close = models.DecimalField(max_digits=12, decimal_places=2)
	high = models.DecimalField(max_digits=12, decimal_places=2)
	low = models.DecimalField(max_digits=12, decimal_places=2)
	date = models.DateField()

	class Meta:
		db_table = 'stock'
		verbose_name = 'stock'
		verbose_name_plural = 'stocks'
		constraints = [
			models.UniqueConstraint(fields=['code', 'date'],
				name='unique_code_date_usd')
		]

	def __str__(self):
		return f'{self.code} O:{self.open} L:{self.low} H:{self.high}'\
				f' C:{self.close} at {self.date}'
