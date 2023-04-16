
#
#The regular expression matches a string that starts with one or more alphanumeric characters or hyphens, followed by a period.
#The target variable is set to the value of the target query parameter.
#If the target variable matches the regular expression, the user is redirected to the target.
#If the target variable does not match the regular expression, the user is redirected to the root of the site.
#
#"""


import re

def redirect_secure(target):
    if not re.match("^[a-zA-Z0-9\-\.]+$", target):
        return "/"

    return target