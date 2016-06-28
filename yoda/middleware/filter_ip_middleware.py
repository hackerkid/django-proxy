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
        """Parse out the subdomain from the request"""
        request.subdomain = None
        host = request.META.get('HTTP_HOST', '')
        host_s = host.replace('www.', '').split('.')
        if len(host_s) > 2:
            request.subdomain = ''.join(host_s[:-2])