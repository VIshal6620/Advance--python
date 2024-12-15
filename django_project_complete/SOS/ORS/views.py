from django.contrib.sessions.models import Session
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .ctl.RegistrationCtl import RegistrationCtl


@csrf_exempt
def action(request,page):
    ctlName = page + "Ctl()"
    ctlobj = eval(ctlName)
    return ctlobj.execute(request,{"id":0})

@csrf_exempt
def auth(request,page="", operation="",id=0):
    if page == "Logout":
        Session.objects.all().delete()
        request.session['user']=None
        ctlName = "Login" + "Ctl()"
        ctlobj = eval(ctlName)
        res = ctlobj.execute(request, {"id":id,"operation":operation})
    return res

def index(request):
    res = render(request,'Welcome.html')
    return res
