from django.db import models


class ExchangeRate(models.Model):

	# variation = models.DecimalField(max_digits=4, decimal_places=2)
	from_currency = models.ForeignKey(
		'currency.Currency',
		on_delete=models.CASCADE,
		related_name='from_rates'
	)
	to_currency = models.ForeignKey(
		'currency.Currency',
		on_delete=models.CASCADE,
		related_name='to_rates'
	)
	open = models.DecimalField(max_digits=12, decimal_places=2)
	close = models.DecimalField(max_digits=12, decimal_places=2)
	high = models.DecimalField(max_digits=12, decimal_places=2)
	low = models.DecimalField(max_digits=12, decimal_places=2)
	date = models.DateField()

	class Meta:
		db_table = 'exchange_rate'
		verbose_name = 'exchange_rate'
		verbose_name_plural = "exchange_rates"

	def __str__(self):
		return f'O:{self.open} L:{self.low} H:{self.high} C:{self.close} at {self.date}'
