from django.contrib import admin

# Register your models here.
from django.contrib.gis import admin
from . import models

class AreaAdmin(admin.GeoModelAdmin):

 search_fields = ['identifier','label']
 list_display = ['identifier', 'label','mpoly']


class LampAdmin(admin.GeoModelAdmin):

 search_fields = ['identifier']
 list_display = ['identifier','mpoint']

admin.site.register(models.Area,AreaAdmin)
admin.site.register(models.Lamp,LampAdmin)



