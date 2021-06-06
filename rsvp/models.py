from django.db import models
from core.models import TimeStampedModel
import datetime
import phonenumbers


class RSVP(TimeStampedModel):
    email = models.EmailField(max_length=256, unique=True, db_index=True)
    telephone = models.CharField(max_length=16, blank=True)
    num_guests_allowed = models.SmallIntegerField(default=2)
    location = models.TextField(blank=True)
    message = models.TextField(blank=True)

    def format_number(self):
        try:
            n = phonenumbers.parse(self.telephone, "US")
            output = phonenumbers.format_number(n, phonenumbers.PhoneNumberFormat.NATIONAL)
            return output
        except:
            return self.telephone

    format_number.short_description = "Telephone"

    formatted_telephone = property(format_number)

    def __unicode__(self):
        return "%s [%d]" % (self.email, self.id)


class AccessCode(models.Model):
    rsvp = models.ForeignKey(RSVP, on_delete=models.CASCADE)
    access_code = models.CharField(max_length=8)
    created = models.DateTimeField(auto_now_add=True)
    expires = models.DateTimeField()

    def extend(self):
        expires = datetime.datetime.utcnow() + datetime.timedelta(hours=48)
        self.expires = expires
        self.save()

"""
class Meal(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
"""
""" beef, chicken, vegitarian """

MEALS = (
    (0, "I don't care, surprise me!"),
    (1, "Beef"),
    (2, "Chicken"),
    (3, "Vegetarian")
)


class Guest(models.Model):
    rsvp = models.ForeignKey(RSVP, on_delete=models.CASCADE, related_name="guests")
    name = models.CharField(max_length=128)
    meal = models.SmallIntegerField(choices=MEALS)
    notes = models.TextField(blank=True)


class NotAttending(models.Model):
    rsvp = models.ForeignKey(RSVP, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    message = models.TextField(blank=True)
