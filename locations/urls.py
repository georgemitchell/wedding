import views

from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.index, name="locations"),
    url(r'^traverse_city', views.traverse_city, name="traverse_city"),
    url(r'^leelanau', views.leelanau, name="leelanau"),
    url(r'^old_mission', views.old_mission, name="old_mission"),
    url(r'^search', views.search, name="search"),
    url(r'^wines', views.wines, name="wines"),
]
