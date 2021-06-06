from django.conf.urls import url
from django.urls import include, path
import rsvp.views as views

urlpatterns = [
    path('', views.email_check, name="email_check"),
    path('details/(?P<pk>\d+)/(?P<access_code>.+)/$', views.RSVPDetails.as_view(), name="ajax_rsvp_details"),
    path('details/(?P<pk>\d+)/$', views.RSVPDetails.as_view(), name="ajax_rsvp_details"),
    path('ajax/access_code/(?P<pk>\d+)/$', views.ajax_access_code, name="ajax_access_code"),
    path('ajax/details/(?P<pk>\d+)/$', views.AjaxRSVPDetails.as_view(), name="ajax_rsvp_details"),
    path('ajax/email_check/$', views.AjaxEmailCheck.as_view(), name='ajax_email_check'),
    path('email/access_code/$', views.access_email, name='access_email'),
    path('send_confirmation/(?P<rsvp_id>\d+)/(?P<access_code>.+)/$', views.send_confirmation, name='send_confirmation'),
    path('send_link/(?P<rsvp_id>\d+)/$', views.send_link, name='send_link'),
]
