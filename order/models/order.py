from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
  cliente = models.ForeignKey(
		User,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		verbose_name="Cliente"
	)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return "Pedido: #{}".format(self.id)

  class Meta:
    app_label="order"
    verbose_name="Pedido"
    verbose_name_plural="Pedidos"