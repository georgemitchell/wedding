import views

from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.RSVPCreateView.as_view(), name='rsvp'),
]