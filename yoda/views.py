from django.http import HttpResponse, HttpResponseNotFound

def hello(request):
    domain = request.META.get('HTTP_HOST') or request.META.get('SERVER_NAME')
    return HttpResponse('You are in' + domain)