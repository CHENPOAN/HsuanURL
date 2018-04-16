from django.conf import settings
from django.http import HttpResponseRedirect

# getattr(對象, 屬性, 預設回傳值)
# DEFAULT_REDIRECT_URL = getattr(settings, "DEFAULT_REDIRECT_URL", "http://www.hsuan.com:8000")
DEFAULT_REDIRECT_URL = getattr(settings, "DEFAULT_REDIRECT_URL")

def wildcard_redirect(request, path=None):
    new_url = DEFAULT_REDIRECT_URL
    if path is not None:
        new_url = DEFAULT_REDIRECT_URL + "/" + path
    return HttpResponseRedirect(new_url)