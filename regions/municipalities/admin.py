from django.contrib import admin

from .models import Region, Municipality, MunicipalityXRegion

admin.site.register(Municipality)
admin.site.register(Region)
admin.site.register(MunicipalityXRegion)
