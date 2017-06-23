from django.core.management.base import BaseCommand, CommandError
from locations.models import Destination
import json
import urllib
import urllib2
import time
import random

GOOGLE_API = "http://maps.googleapis.com/maps/api/geocode/json?address=%s"


def retrieve_data(url):
    print url
    contents = urllib2.urlopen(url).read()
    data = json.loads(contents)
    if "status" not in data:
        print "Problem with retrieved data"
        print data
        return None
    if data["status"] != "OK":
        print "Problem with retrieved data"
        print data
        return None
    if "results" not in data:
        print "Problem with retrieved data"
        print data
        return None
    return data["results"]


class Command(BaseCommand):
    help = 'Uses google api to update lat/lng for untagged destinations'

    def handle(self, *args, **options):
        destinations = Destination.objects.filter(latitude__isnull=True)
        print "Found %d destinations that need to be updated" % len(destinations)
        for destination in destinations:
            url_encoded_address = urllib.quote(destination.address)
            url = GOOGLE_API % url_encoded_address
            data = retrieve_data(url)
            if data is None:
                return
            if len(data) == 0:
                print "No results found for %s" % destination.address
            else:
                result = data[0]
                if "geometry" in result:
                    if "location" in result["geometry"]:
                        location = result["geometry"]["location"]
                        destination.latitude = location["lat"]
                        destination.longitude = location["lng"]
                        destination.save()
                        print "Updated %s [%d]" % (destination.name, destination.id)
                else:
                    print "Unexpected output:"
                    print result

            throttle = random.randint(5,15)
            print "Pausing %d seconds to prevent blasting the api" % throttle
            time.sleep(throttle)


