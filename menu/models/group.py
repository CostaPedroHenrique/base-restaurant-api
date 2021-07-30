from django.db import models

class Group(models.Model):
  name = models.CharField(
    max_length=70,
    verbose_name='Nome',
    null=False
  )

  description = models.TextField(
    verbose_name="Descrição",
    null=False
  )

  icon = models.ImageField(
    verbose_name="Ícone",
    upload_to="group_icons",
    null=False
  )



  def __str__(self):
    return self.name

  class Meta:
    app_label="menu"
    verbose_name="Grupo"
    verbose_name_plural="Grupos"