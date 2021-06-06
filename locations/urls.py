import locations.views as views
from django.urls import include, path

urlpatterns = [
    path('', views.index, name="locations"),
    path('traverse_city/', views.traverse_city, name="traverse_city"),
    path('leelanau/', views.leelanau, name="leelanau"),
    path('old_mission/', views.old_mission, name="old_mission"),
    path('search/', views.search, name="search"),
    path('wines/', views.wines, name="wines"),
]
