
#
#The regular expression is compiled once, when the module is loaded.
#The regular expression is used to match the target URL.
#If the target URL matches, it is used as the redirect target.
#If the target URL does not match, a default URL is used.
#The regular expression is not used to construct the redirect URL.
#


import re

from . import base

class Redirect(base.Redirect):
    """Redirect to a URL based on the target URL.

    The URL is constructed by replacing the part of the target URL that
    matches the regular expression with the replacement string.

    """

    def __init__(self, regex, replacement, default=None):
        """Initialize the redirect.

        The regex argument is the regular expression to match the target URL.
        The replacement argument is the string to replace the matched part of
        the target URL.
        The default argument is the URL to use if the target URL does not match
        the regular expression.

        """
        self.regex = re.compile(regex)
        self.replacement = replacement
        self.default = default

    def get_url(self, request):
        """Return the redirect URL.

        The redirect URL is constructed by replacing the part of the target
        URL that matches the regular expression with the replacement string.
        If the target URL does not match the regular expression, the default
        URL is used.

        """
        match = self.regex.search(request.url)
        if match:
            return request.url.replace(match.group(0), self.replacement)
        else:
            return self.default