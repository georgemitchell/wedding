from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.email_check, name="email_check"),
    url(r'^details/(?P<pk>\d+)/(?P<access_code>.+)/$', views.RSVPDetails.as_view(), name="ajax_rsvp_details"),
    url(r'^details/(?P<pk>\d+)/$', views.RSVPDetails.as_view(), name="ajax_rsvp_details"),
    url(r'^ajax/access_code/(?P<pk>\d+)/$', views.ajax_access_code, name="ajax_access_code"),
    url(r'^ajax/details/(?P<pk>\d+)/$', views.AjaxRSVPDetails.as_view(), name="ajax_rsvp_details"),
    url(r'^ajax/email_check/$', views.AjaxEmailCheck.as_view(), name='ajax_email_check'),
    url(r'^email/access_code/$', views.access_email, name='access_email'),
    url(r'^send_confirmation/(?P<rsvp_id>\d+)/(?P<access_code>.+)/$', views.send_confirmation, name='send_confirmation'),
    url(r'^send_link/(?P<rsvp_id>\d+)/$', views.send_link, name='send_link'),
]
