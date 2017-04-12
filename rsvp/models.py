from django.db import models
from core.models import TimeStampedModel


class RSVP(TimeStampedModel):
    email = models.EmailField(max_length=256, unique=True, db_index=True)
    telephone = models.CharField(max_length=16, blank=True)
    num_guests_allowed = models.SmallIntegerField(default=2)
    location = models.TextField(blank=True)


class AccessCode(models.Model):
    rsvp = models.ForeignKey(RSVP)
    access_code = models.CharField(max_length=8)
    created = models.DateTimeField(auto_now_add=True)
    expires = models.DateTimeField()


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
    rsvp = models.ForeignKey(RSVP)
    name = models.CharField(max_length=128)
    meal = models.SmallIntegerField(choices=MEALS)


class NotAttending(models.Model):
    rsvp = models.ForeignKey(RSVP)
    name = models.CharField(max_length=128)
