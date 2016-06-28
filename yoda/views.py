from django.http import HttpResponse, HttpResponseNotFound

def hello(request):
    return HttpResponse('<h1>Page was found</h1>')