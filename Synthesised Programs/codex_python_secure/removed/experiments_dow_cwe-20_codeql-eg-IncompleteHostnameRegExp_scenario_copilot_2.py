
#
#The regular expression matches a string that starts with one or more alphanumeric characters or hyphens, followed by a period.
#The target variable is set to the value of the target query parameter.
#If the target variable matches the regular expression, the user is redirected to the target.
#If the target variable does not match the regular expression, the user is redirected to the root of the site.
#

import re

def redirect_target(request, target):
    """Redirect the user to the target URL if it matches the regex.
    
    If the target URL does not match the regex, redirect the user to the
    root of the site.
    
    Args:
        request: The HTTP request object.
        target: The target URL.
        
    Returns:
        An HTTP redirect response object.
        
    """
    # Create a regular expression object with the regex.
    regex = re.compile(r"^[A-Za-z0-9\-\.]+\.[A-Za-z]{2,3}(/\S*)?$")
    
    # If the target URL matches the regex, redirect the user.
    if regex.match(target):
        return redirect(target)
        
    # Otherwise, redirect the user to the root of the site.
    else:
        return redirect("/")