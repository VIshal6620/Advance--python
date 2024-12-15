from django.shortcuts import render

from SOS.ORS.ctl.BaseCtl import BaseCtl


class WelcomeCtl(BaseCtl):
    def display(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form})

    def get_template(self):
        return "welcome.html"

    def get_service(self):
        return "RoleService()"
