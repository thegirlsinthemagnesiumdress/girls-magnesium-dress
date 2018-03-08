from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="public/index.html"), name="index"),
    url(r'^register$', TemplateView.as_view(template_name="public/register.html"), name="register")
]
