from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from djangae.environment import is_production_environment
from core import views
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns


admin.autodiscover()


urlpatterns = [
    url(r'^_ah/', include('djangae.urls')),
    url(r'^_ah/bounce$', views.receive_bounce, name="email-bounce"),
    # Note that by default this is also locked down with login:admin in app.yaml
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('djangae.contrib.gauth.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^cron/pull_qualtrics_results/$', views.sync_qualtrics_results, name="pull-qualtrics-results"),
    url(r'^cron/generate_exports/$', views.generate_exports_task, name="export-datastore-data"),
    url(r'^cron/update_benchmarks/$', views.update_industries_benchmarks_task, name="update-benchmarks"),
    url(r'^migrations/migrate_to_dmblite_survey/$', views.update_survey_model_task, name="migrate_to_dmblite_survey"),
    url(r'^migrations/resave_surveys/$', views.resave_surveys_task, name="resave_surveys"),
    url(r'^migrations/drop_search_index/$', views.drop_search_index_task, name="drop_search_index"),
    url(r'^migrations/import_lite_users_and_accounts/$', views.import_lite_users_and_accounts, name="import_lite_users_and_accounts"), # noqa
    url(r'^migrations/link_surveys/$', views.link_surveys_task, name="link_surveys"),
    url(r'^(?P<tenant>{})/'.format(settings.NOT_I18N_TENANTS), include('public.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns(
    url(r'', include('public.urls', namespace="legacy")),  # handle all the old links before the introduction of tenants concept  # noqa
    url(r'^(?P<tenant>{})/'.format(settings.I18N_TENANTS), include('public.urls')),
    url(r'^angular/(?P<template_name>{})/$'.format(settings.ALLOWED_ANGULAR_TEMPLATES), views.angular_templates, name="angular-templates"),  # noqa
    )

handler404 = 'public.views.handler404'
handler500 = 'public.views.handler500'

# Only enable static serving locally, on prod we use app.yaml
if not is_production_environment():
    urlpatterns += static(settings.STATIC_URL, serve)
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
