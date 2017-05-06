from django.contrib import admin

# Register your models here.
from models import RSVP, NotAttending, Guest


class RSVPAdmin(admin.ModelAdmin):
    list_display = ('email', 'formatted_telephone', 'location', 'message')
    pass


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'meal', 'notes', 'rsvp')
    pass


admin.site.register(RSVP, RSVPAdmin)
admin.site.register(Guest, GuestAdmin)
