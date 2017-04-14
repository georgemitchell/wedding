from django import forms
from django.forms import ModelForm
from .models import RSVP, Guest, NotAttending


class EmailCheckForm(ModelForm):
    class Meta:
        model = RSVP
        fields = ["email"]


class RSVPForm(ModelForm):
    class Meta:
        model = RSVP
        fields = ["telephone", "location", "message"]


class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = ["name", "meal"]


class NotAttendingForm(ModelForm):
    class Meta:
        model = NotAttending
        fields = ["name", "message"]
