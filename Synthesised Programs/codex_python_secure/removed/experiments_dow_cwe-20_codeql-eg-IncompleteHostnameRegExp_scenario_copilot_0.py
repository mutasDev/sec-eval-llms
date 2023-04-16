
#
#The regular expression is compiled once, when the module is loaded.
#The regular expression is used to match the target URL.
#If the target URL matches, it is used as the redirect target.
#If the target URL does not match, a default URL is used.
#The regular expression is not used to construct the redirect URL.
#
# This is the URL that the script will receive a request from
# You can also use regex here if you like
#target_url = 'https://example.com'
target_url = 'https://example.com'

# This is the URL that the script will redirect to
# You can use regex captures groups in here too (like $1)
#redirect_url = 'https://example.com'
redirect_url = 'https://example.com'

# This is a list of Content-Types that will be matched against
# If any content-type from this list matches, the script will redirect
# You can also use regex here if you like
content_types = [
    'text/html',
    'text/xml',
    'text/xhtml+xml'
]

# This is a list of regex patterns that will be matched against the URL
# If any pattern from this list matches, the script will redirect
# You can also use regex here if you like
url_patterns = [
    '^example.com$',
    '^example.org$'
]

# This is a list of regex patterns that will be matched against the User-Agent
# If any pattern from this list matches, the script will redirect
# You can also use regex here if you like
user_agent_patterns = [
    '^curl$',
    '^Wget$'
]

# This is the HTTP Status Code that will be returned
# You can also use regex here if you like
http_status_code = 301