from django.contrib import admin

# Register your models here.
from rsvp.models import RSVP, NotAttending, Guest


class RSVPAdmin(admin.ModelAdmin):
    list_display = ('email', 'formatted_telephone', 'location', 'message')
    pass


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'meal', 'notes', 'rsvp')
    pass


class NotAttendingAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'rsvp')
    pass

admin.site.register(RSVP, RSVPAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(NotAttending, NotAttendingAdmin)
