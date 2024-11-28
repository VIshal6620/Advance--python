from django.http import HttpResponse


def sos_home(request):
    return HttpResponse("<h1>SOS Applicatin</h1>")
