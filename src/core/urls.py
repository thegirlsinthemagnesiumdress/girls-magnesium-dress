from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from djangae.environment import is_production_environment
from core import views
import session_csrf
session_csrf.monkeypatch()

from django.contrib import admin
admin.autodiscover()

import public.urls
import api.urls

urlpatterns = [
    url(r'^_ah/', include('djangae.urls')),

    # Note that by default this is also locked down with login:admin in app.yaml
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('djangae.contrib.gauth.urls')),
    url(r'', include(public.urls)),
    url(r'^api/', include(api.urls)),
    url(r'^cron/pull_qualtrics_results/$', views.sync_qualtrics_results, name="pull-qualtrics-results"),
    url(r'^cron/generate_export/$', views.generate_export, name="export-datastore-data"),
]

# Only enable static serving locally, on prod we use app.yaml
if not is_production_environment():
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
