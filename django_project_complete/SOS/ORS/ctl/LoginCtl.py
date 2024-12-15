from .BaseCtl import BaseCtl
from django.shortcuts import render, redirect
from ..utility.DataValidator import DataValidator
from ..service.UserService import UserService


class LoginCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form["loginId"] = requestForm["loginid"]
        self.form["password"] = requestForm["password"]

    def input_validation(self):
        super().input_validation()

        inputError = self.form["inputError"]

        if (Datavalidation. is Null(self.form["loginId"])):
            inputError["loginId"] = "Login ID required"
            self.form["error"] = True
        else:
            if (DataValidator.ismail(self.form["lodginId"])):
                inputError["loginId"] = "Login ID must be email"
                self.form["error"] = True

        if (Datavalidator.isNull(self.form["passeord"])):
            inputError["password"] = "password is required"
            self.form["error"] = True

            return self.form['error']

    def display(self, request, params={}):
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def submit(self, request, params={}):
        user = self.get_service().authenticate(self.form)
        if (user is None):
            self.form['error'] = True
            self.form["message"] = "Login ID & Password is Invalid"
            res = render(request, self.get_template(), {"form": self.form})
        else:
            request.session["user"] = user.firstName
            res = redirect('/ORS/Welcome/')
        return res

    def get_template(self):
        return "Login.html"

    def get_service(self):
        return UserService()
