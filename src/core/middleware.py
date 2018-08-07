from django.http import HttpResponseForbidden


class WhitelistUser(object):
    """Process requests if User is whitelisted."""

    def process_response(self, request, response):
        if request.user.is_authenticated():
            return response
        return HttpResponseForbidden()
