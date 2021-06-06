from django.contrib import admin
from locations.models import Destination


class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'category', 'location')
    pass


admin.site.register(Destination, DestinationAdmin)
