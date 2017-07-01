function initMap() {
  var traverse_city = {lat: 44.7633946, lng: -85.61752840000001};
  var map = new google.maps.Map(document.getElementById('map'), {
      center: traverse_city,
      styles: [
    {
        "featureType": "administrative",
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "color": "#444444"
            }
        ]
    },
    {
        "featureType": "administrative.country",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "visibility": "on"
            }
        ]
    },
    {
        "featureType": "landscape",
        "elementType": "all",
        "stylers": [
            {
                "color": "#f2f2f2"
            }
        ]
    },
    {
        "featureType": "landscape",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#ecddbb"
            }
        ]
    },
    {
        "featureType": "landscape.natural",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "visibility": "on"
            },
            {
                "color": "#d9d8b2"
            }
        ]
    },
    {
        "featureType": "landscape.natural.terrain",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#e1d0ad"
            }
        ]
    },
    {
        "featureType": "poi",
        "elementType": "all",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "road",
        "elementType": "all",
        "stylers": [
            {
                "saturation": -100
            },
            {
                "lightness": 45
            }
        ]
    },
    {
        "featureType": "road",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#9f8e7a"
            }
        ]
    },
    {
        "featureType": "road",
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "color": "#7d7971"
            }
        ]
    },
    {
        "featureType": "road",
        "elementType": "labels.text.stroke",
        "stylers": [
            {
                "color": "#f3e0c1"
            }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "all",
        "stylers": [
            {
                "visibility": "simplified"
            }
        ]
    },
    {
        "featureType": "road.arterial",
        "elementType": "labels.icon",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "road.local",
        "elementType": "geometry.stroke",
        "stylers": [
            {
                "color": "#d5c2a3"
            }
        ]
    },
    {
        "featureType": "transit",
        "elementType": "all",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "water",
        "elementType": "all",
        "stylers": [
            {
                "color": "#46bcec"
            },
            {
                "visibility": "on"
            }
        ]
    },
    {
        "featureType": "water",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#a5d2c9"
            }
        ]
    },
    {
        "featureType": "water",
        "elementType": "geometry.stroke",
        "stylers": [
            {
                "visibility": "on"
            }
        ]
    },
    {
        "featureType": "water",
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "color": "#838383"
            }
        ]
    },
    {
        "featureType": "water",
        "elementType": "labels.text.stroke",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    }
]


    });
  var bounds = new google.maps.LatLngBounds();

  var points = [
  {% for destination in destinations %}
    ['{{ destination.name }}', {{ destination.latitude }}, {{ destination.longitude }}, '{{ destination.icon }}']{% if not forloop.last %},{% endif %}
  {% endfor %}
  ]

  var icons = {
    hotel: {
      icon: '/static/img/hotel.png'
    },
    bandb: {
      icon: '/static/img/bandb.png'
    },
    wineglass: {
      icon: '/static/img/winery-icon.png'
    },
    shop: {
      icon: '/static/img/shop.png'
    },
    food: {
      icon: '/static/img/food.png'
    },
    attraction: {
      icon: '/static/img/camera-icon.png'
    }
  };
  var shape = {
      coord: [1, 1, 1, 20, 18, 20, 18 , 1],
      type: 'poly'
  };

  for (var i=0; i<points.length; i++)
  {
    var latlng = new google.maps.LatLng(points[i][1], points[i][2]);
    var marker = new google.maps.Marker({
      position: latlng,
      map: map,
      title: points[i][0],
      icon: icons[points[i][3]].icon,
      shape: shape
    });
    bounds.extend(latlng);
  }
  map.fitBounds(bounds);
}
