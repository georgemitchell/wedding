from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from core.views import index, archive

urlpatterns = [
    # Examples:
    # url(r'^$', 'reginaandgeorge.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('', index),
    re_path(r'^wedding*', index),
    re_path(r'^locations*', index),
    re_path(r'^rsvp*', index),
    path('archive/', archive),
    path('archive/wedding/', include('core.urls')),
    path('archive/locations/', include('locations.urls')),
    path('archive/admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
