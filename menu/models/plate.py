from django.db import models
from .group import Group


class Plate(models.Model):
  group = models.ForeignKey(
    Group,
    name="Grupo",
    on_delete=models.CASCADE
  )

  name = models.CharField(
    max_length=100,
    verbose_name="Nome",
    null=False
  )

  description = models.CharField(
    max_length=100,
    verbose_name="Descrição",
    null=False
  )

  price = models.DecimalField(
    verbose_name="Preço",
    max_digits=5,
    decimal_places=2,
    null=False
  )

  available = models.BooleanField(
    verbose_name="Disponível",
    default=True,
  )

  photo = models.ImageField(
    verbose_name="Ícone",
    upload_to="group_icons",
    null=False
  )

  def __str__(self):
    return self.name

  class Meta:
    app_label="menu"
    verbose_name="Prato"
    verbose_name_plural="Pratos"