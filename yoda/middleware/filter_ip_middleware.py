from django.http import HttpResponseForbidden, HttpResponseRedirect
from yoda.models import *

class FilterIPMiddleware(object):
    def process_request(self, request):
        allowed_ips = ['127.0.0.1', '123.123.123.123'] # Authorized ip's
        ip = request.META.get('REMOTE_ADDR') # Get client IP
        if ip not in allowed_ips:
            return HttpResponseForbidden()
        return None

class RedirectMiddleware(object):
    """Middleware class that redirects non "www" subdomain requests to a
    specified URL or business.
    """
    def process_request(self, request):
        """Returns an HTTP redirect response for requests including non-"www"
        subdomains.
        """
        scheme = "http" if not request.is_secure() else "https"
        path = request.get_full_path()
        domain = request.META.get('HTTP_HOST') or request.META.get('SERVER_NAME')
        pieces = domain.split('.')
        subdomain = ".".join(pieces[:-2]) # join all but primary domain
        default_domain = "www"
        if domain in {default_domain, "testserver", "localhost"}:
            return HttpResponseForbidden()
        try:
            route = Subdomain.objects.get(name=subdomain).url
        except Subdomain.DoesNotExist:
            route = path
        return HttpResponseRedirect("{0}://{1}{2}".format(
            scheme, domain, route))