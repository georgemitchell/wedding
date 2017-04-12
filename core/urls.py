import views

from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^couple', views.couple, name="couple"),
    url(r'^story', views.story, name="story"),
    url(r'^people', views.people, name="people"),
    url(r'^wedding', views.wedding, name="wedding"),
    url(r'^gifts', views.gifts, name="gifts"),
    url(r'^rsvp/', include('rsvp.urls')),
    url(r'^travel', views.travel, name="travel"),
    url(r'^traverse_city', views.traverse_city, name="traverse_city"),
    url(r'^leelanau', views.leelanau, name="leelanau"),
    url(r'^old_mission', views.old_mission, name="old_mission"),
    #url(r'^$', views.RSVPCreateView.as_view(), name='rsvp'),
]