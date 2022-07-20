from django.db import models


class Company(models.Model):

	name = models.CharField(max_length=100, null=False, blank=False)
	code = models.CharField(max_length=5, null=False, unique=True)

	class Meta:
		db_table = "company"
		verbose_name = "company"
		verbose_name_plural = "companies"

	def __str__(self):
		return f"{self.code}:{self.name}"
