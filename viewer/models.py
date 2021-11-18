from django.db import models


class ViewTable(models.Model):
    order_date = models.DateField()
    region = models.CharField(max_length=30)
    rep = models.CharField(max_length=30)
    item = models.CharField(max_length=30)
    quantity = models.IntegerField()
    total_discount = models.DecimalField(max_digits=10, decimal_places=2)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['order_date']


