from django.contrib.admindocs.utils import default_reference_role
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session

from .ctl.RegistrationCtl import RegistrationCtl
from .ctl.LoginCtl import LoginCtl
from .ctl.WelcomeCtl import WelcomeCtl
from .ctl.UserCtl import UserCtl
from .ctl.RoleCtl import RoleCtl
from .ctl.UserListCtl import UserListCtl
from .ctl.ForgetPasswordCtl import ForgetPasswordCtl
from .ctl.AttributeCtl import AttributeCtl
from .ctl.AttributeListCtl import AttributeListCtl
from .ctl.InitiativeCtl import InitiativeCtl
from .ctl.InitiativeListCtl import InitiativeListCtl
from .ctl.EmployeeCtl import EmployeeCtl
from .ctl.EmployeeListCtl import EmployeeListCtl
from .ctl.ClientCtl import ClientCtl
from .ctl.ClientListCtl import ClientListCtl
from .ctl.PhysicianCtl import PhysicianCtl
from .ctl.PhysicianListCtl import PhysicianListCtl
from .ctl.MedicationCtl import MedicationCtl
from .ctl.MedicationListCtl import MedicationListCtl
from .ctl.Follow_UpCtl import Follow_UpCtl
from .ctl.Follow_UpListCtl import Follow_UpListCtl
from .ctl.Staff_MemberCtl import Staff_MemberCtl
from .ctl.Staff_MemberListCtl import Staff_MemberListCtl
from .ctl.PositionCtl import PositionCtl
from .ctl.PositionListCtl import PositionListCtl
from .ctl.CustomerCtl import CustomerCtl
from .ctl.CustomerListCtl import CustomerListCtl

@csrf_exempt
def action(request, page="", operation="", id=0):
    if page == "Logout":
        Session.objects.all().delete()
        request.session['user'] = None
        page = "Login"
    ctlName = page + "Ctl()"
    ctlObj = eval(ctlName)
    res = ctlObj.execute(request, {"operation": operation, "id": id})
    return res


def index(request):
    res = render(request, 'Welcome.html')
    return res
