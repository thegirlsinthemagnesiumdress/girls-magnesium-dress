from core.settings.local import *  # noqa


def patch_django_angular_render():
    from django.shortcuts import render as django_render
    from angular import shortcuts
    from angular.templatetags.angular import DjangoBlockNode

    shortcuts.render = django_render
    DjangoBlockNode.render = lambda x, y: ''


patch_django_angular_render()
