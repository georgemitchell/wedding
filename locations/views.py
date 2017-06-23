# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from models import Destination, Location, Category


def index(request):
    template = loader.get_template('locations/places.html')
    return HttpResponse(template.render(Context({})))


def search(request):
    category_id = int(request.GET.get("category_id", 0))
    location_id = int(request.GET.get("location_id", 0))
    destinations = Destination.objects.all()
    if category_id > 0:
        destinations = destinations.filter(category=category_id)

    if location_id > 0:
        destinations = destinations.filter(location=location_id)

    destinations = destinations.order_by("name")
    template = loader.get_template('locations/search.html')
    categories = Destination.CATEGORIES
    locations = Destination.LOCATIONS
    context = {
        "destinations": destinations,
        "categories": categories,
        "locations": locations,
        "category": category_id,
        "location": location_id
    }
    return HttpResponse(template.render(Context(context)))


def get_destinations(location_id, categories, headings):
    qs = Destination.objects.filter(location=location_id)
    destinations = {}
    for result in qs:
        if result.category not in destinations:
            destinations[result.category] = []
        destinations[result.category].append(result)
    output = []
    for category_id in categories:
        if category_id in destinations:
            category = destinations[category_id][0].get_category_display()
            entry = {"name": category, "destinations": destinations[category_id]}
            if category_id in headings:
                entry["heading"] = headings[category_id]
            output.append(entry)
    return output


def traverse_city(request):
    categories = [
        Category.Shop.id,
        Category.Food.id,
        Category.Attraction.id,
        Category.Winery.id,
        Category.Hotel.id
    ]
    headings = {
        Category.Shop.id: """There is a three-block stretch between Boardman and Union Streets, 
                             packed with dozens of boutiques, gourmet food purveyors, indie bookstores,
                             cafes, and restaurants. Take time to wander down the side streets and 
                             alleys to find off-the-beaten path shops. Regina and her parents come 
                             here often, and the Farmers’ Market on Saturday mornings is a wonderful treat!""",
        Category.Hotel.id: """George's mother will be hosting the rehearsal dinner for all out-of-town guests at
                              <a href="http://www.cornerlofttc.com/" target="_blank">The Corner Loft</a>,
                              which is in the heart of downtown.  Staying downtown would give you dozens of
                              hotels from which to choose and put you close to all the festivities. 
                              We love visiting the fun shops on Front Street and the Farmers' Market each Saturday.
                              Traverse City has also become a foodie destination (you can read about
                              <a href="http://www.fodors.com/news/mario-batalis-top-summer-destinations-for-foodies-5751" target="_blank">Mario Batali's favorite places</a>),
                              and is now home to trendy breweries and distilleries, cute coffee shops, and wonderful restaurants. 
                              If you stay downtown, you will be within walking distance to the rehearsal dinner,
                              20 minutes from the wedding site, and 20 minutes from my parents' house."""
    }

    destinations = get_destinations(Location.TraverseCity.id, categories, headings)
    template = loader.get_template('locations/traverse_city.html')
    return HttpResponse(template.render(Context({"destinations": destinations})))


def leelanau(request):
    categories = [
        Category.Shop.id,
        Category.Food.id,
        Category.Attraction.id,
        Category.Winery.id,
        Category.Hotel.id
    ]
    headings = {
        Category.Winery.id: 'They are all fun! If you can only visit a couple, don’t miss <a href="https://www.bonobowinery.com/" target="_blank">Bonobo</a> and <a href="http://www.chateauchantal.com/" target="_blank">Chateau Chantal</a>.',
    }

    destinations = get_destinations(Location.Leelanau.id, categories, headings)
    template = loader.get_template('locations/leelanau.html')
    return HttpResponse(template.render(Context({"destinations": destinations})))


def old_mission(request):
    categories = [
        Category.Shop.id,
        Category.Food.id,
        Category.Attraction.id,
        Category.Winery.id,
        Category.BedAndBreakfast.id
    ]
    headings = {
        Category.Winery.id: 'They are all fun! If you can only visit a couple, don’t miss <a href="https://www.bonobowinery.com/" target="_blank">Bonobo</a> and <a href="http://www.chateauchantal.com/" target="_blank">Chateau Chantal</a>.',
        Category.BedAndBreakfast.id: 'Old Mission has become a destination for couples seeking a romantic getaway. Unfortunately, this means no children in most places. If, however, you are sans children or planning to leave the kids at home, Old Mission will be the perfect place to stay.'
    }
    destinations = get_destinations(Location.OldMission.id, categories, headings)
    template = loader.get_template('locations/old_mission.html')
    return HttpResponse(template.render(Context({"destinations": destinations})))


def wines(request):
    destinations = Destination.objects.filter(category=Category.Winery.id).order_by("name")
    template = loader.get_template('locations/wines.html')
    return HttpResponse(template.render(Context({"destinations": destinations})))
