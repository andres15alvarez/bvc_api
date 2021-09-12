from django.db import models


class IBC(models.Model):

	date = models.DateField()
	ibc = models.DecimalField(max_digits=12, decimal_places=2)

	class Meta:
		ordering = ['-date']

	def __str__(self):
		return str(self.ibc)
