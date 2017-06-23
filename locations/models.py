from django.db import models


class Location:
    class OldMission:
        id = 1
        name = "Old Mission"
        static_image = "om_square.jpg"

    class TraverseCity:
        id = 2
        name = "Traverse City"
        static_image = "tc_square.jpg"

    class Leelanau:
        id = 3
        name = "Leelanau"
        static_image = "l_square.jpg"


class Category(object):
    class Base:
        def __init__(self):
            self.destinations = []

    class Hotel(Base):
        id = 1
        name = "Hotels"
        icon = "hotel"

    class BedAndBreakfast(Base):
        id = 2
        name = "Bed & Breakfasts"
        icon = "bandb"

    class Winery(Base):
        id = 3
        name = "Wineries"
        icon = "wineglass"

    class Shop(Base):
        id = 4
        name = "Shopping"
        icon = "shop"

    class Food(Base):
        id = 5
        name = "Food"
        icon = "food"

    class Attraction(Base):
        id = 6
        name = "Attractions"
        icon = "attraction"

    def __init__(self):
        self.categories = {}

    def append_result(self, result):
        if self.categories[result.category] is None:
            pass


CATEGORY_LOOKUPS = {c.id: c for c in [Category.Hotel, Category.BedAndBreakfast, Category.Winery, Category.Shop, Category.Food, Category.Attraction]}


class Destination(models.Model):
    LOCATIONS = (
        (0, "All Locations"),
        (Location.OldMission.id, Location.OldMission.name),
        (Location.TraverseCity.id, Location.TraverseCity.name),
        (Location.Leelanau.id, Location.Leelanau.name),
    )

    CATEGORIES = (
        (0, "All Categories"),
        (Category.Hotel.id, Category.Hotel.name),
        (Category.BedAndBreakfast.id, Category.BedAndBreakfast.name),
        (Category.Winery.id, Category.Winery.name),
        (Category.Shop.id, Category.Shop.name),
        (Category.Food.id, Category.Food.name),
        (Category.Attraction.id, Category.Attraction.name)
    )
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    location = models.SmallIntegerField(choices=LOCATIONS)
    category = models.SmallIntegerField(choices=CATEGORIES)
    static_image = models.CharField(max_length=128)
    description = models.TextField()
    url = models.URLField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)

    def icon(self):
        return CATEGORY_LOOKUPS[self.category].icon


