from django.http import HttpResponse, HttpResponseNotFound

def hello(request):
    domain = request.META.get('HTTP_HOST') or request.META.get('SERVER_NAME')
    pieces = domain.split('.')
    subdomain = ".".join(pieces[:-2]) # join all but primary domain
    return HttpResponse('You are in ' + subdomain)