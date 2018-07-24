class FetchResultException(Exception):
    """Handle Qualtrics API error message.

    :Attributes:
        status: status returned by Qualtrics API call
        reason: reason retuned by Qualtrics API call
    """
    def __init__(self, json_response):
        meta = json_response.get('meta')
        self.status = meta.get('httpStatus', None)
        self.reason = meta.get('error').get('errorMessage', None)

        super(FetchResultException, self).__init__(
            u"Qualtrics API Exception:`{}`. Reason: {}".format(self.status, self.reason)
        )
