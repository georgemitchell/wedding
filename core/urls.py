import core.views as views

from django.conf.urls import include, url
from django.urls import include, path

urlpatterns = [
    path('', views.archive, name="home"),
    path('couple/', views.couple, name="couple"),
    path('story/', views.story, name="story"),
    path('people/', views.people, name="people"),
    path('wedding/', views.wedding, name="wedding"),
    path('gifts/', views.gifts, name="gifts"),
    path('rsvp/', include('rsvp.urls')),
    path('travel/', views.travel, name="travel"),
    #url(r'^$', views.RSVPCreateView.as_view(), name='rsvp'),
]