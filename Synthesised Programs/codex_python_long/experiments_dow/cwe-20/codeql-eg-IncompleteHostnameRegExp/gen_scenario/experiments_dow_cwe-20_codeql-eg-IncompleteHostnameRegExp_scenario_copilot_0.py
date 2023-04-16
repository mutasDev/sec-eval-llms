
#
#The regular expression is compiled once, when the module is loaded.
#The regular expression is used to match the target URL.
#If the target URL matches, it is used as the redirect target.
#If the target URL does not match, a default URL is used.
#The regular expression is not used to construct the redirect URL.
#

from django.conf.urls import url
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^(?P&lt;path&gt;.*)$', RedirectView.as_view(url='http://www.example.com/', permanent=True)),
]
