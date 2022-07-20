from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True, null=False)
    name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = "currency"
        verbose_name = "currency"
        verbose_name_plural = "currencies"
