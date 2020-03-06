from django.http import HttpResponse





def index(request):
    "First request"
    return HttpResponse("Hello World of Django/ This is polls inex.")
