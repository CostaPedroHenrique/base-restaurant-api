from base_restaurant.order.models.order import Order
from django.db import models
from menu.models import Plate
from .order import Order

class Item(models.Model):
  order = models.ForeignKey(
		Order,
		on_delete=models.CASCADE,
		null=False,
		verbose_name="Pedido"
	)

  plate = models.ForeignKey(
		Plate,
		on_delete=models.SET_NULL,
		null=False,
		verbose_name="Cliente"
	)

  amount = models.IntegerField(
    null=False,
    verbose_name="Quantidade"
  )

