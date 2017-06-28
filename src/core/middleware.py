import cProfile
import pstats

from django.conf import settings
from cStringIO import StringIO


class ProfileMiddleware(object):
    """
        Simple profiling middleware using cProfile
    """
    def process_request(self, request):
        self.prof = None
        if settings.DEBUG and request.GET.has_key('prof'):
            self.prof = cProfile.Profile()
            self.prof.enable()

    def process_response(self, request, response):
        if self.prof:
            self.prof.disable()

            out = StringIO()

            stats = pstats.Stats(self.prof, stream=out).sort_stats('cumulative')
            stats.print_stats()
            stats_str = out.getvalue()

            if response and response.content and stats_str:
                response.content = "<pre>" + stats_str + "</pre>"

            self.prof = None

        return response
