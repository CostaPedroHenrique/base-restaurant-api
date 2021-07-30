from django.contrib import admin

from .models import (Group, Plate)
# Register your models here.

class PlateInline(admin.TabularInline):
  model=Plate
  extra=0


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
  model=Group
  inlines=[PlateInline]
  # list_display='__all__'
