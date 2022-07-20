from django.db import models


class IBC(models.Model):

	date = models.DateField()
	ibc = models.DecimalField(max_digits=12, decimal_places=2)

	class Meta:
		db_table = "ibc"
		verbose_name = "index_bolsa_caracas"
		verbose_name_plural = "indexes_bolsa_caracas"

	def __str__(self):
		return str(self.ibc)
