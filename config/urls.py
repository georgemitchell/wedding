from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from core.views import index

urlpatterns = [
    # Examples:
    # url(r'^$', 'reginaandgeorge.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^wedding/', include('core.urls')),
    url(r'^locations/', include('locations.urls')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
