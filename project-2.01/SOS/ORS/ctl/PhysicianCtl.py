from django.shortcuts import render
from ..Service.PhysicianService import PhysicianService
from ..ctl.BaseCtl import BaseCtl
from ..models import Physician
from ..utility.DataValidator import DataValidator


class PhysicianCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['fullName'] = requestForm['fullName']
        self.form['birthDate'] = requestForm['birthDate']
        self.form['phone'] = requestForm['phone']
        self.form['specialization'] = requestForm['specialization']

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk

        obj.fullName = self.form['fullName']
        obj.birthDate = self.form['birthDate']
        obj.phone = self.form['phone']
        obj.specialization = self.form['specialization']
        return obj

    def model_to_form(self, obj):
        if obj is None:
            return

        self.form['id'] = obj.id
        self.form['fullName'] = obj.fullName
        self.form['birthDate'] = obj.birthDate
        self.form['phone'] = obj.phone
        self.form['specialization'] = obj.specialization

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['fullName'])):
            inputError['fullName'] = "fullName is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['fullName'])):
                inputError['fullName'] = "fullName only contain Letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['birthDate'])):
            inputError['birthDate'] = "birthDate is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isDate(self.form['birthDate'])):
                inputError['birthDate'] = "birthDate only contain Letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['phone'])):
            inputError['phone'] = "phone is Required"
            self.form['error'] = True
        else:
            if (DataValidator.ismobilecheck(self.form['phone'])):
                inputError['phone'] = "phone only contain Letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['specialization'])):
            inputError['specialization'] = "specialization is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['specialization'])):
                inputError['description'] = "specialization only contain Letters"
                self.form['error'] = True

        return self.form['error']

    def display(self, request, params={}):
        if (params['id'] > 0):
            obj = self.get_service().get(params['id'])
            self.model_to_form(obj)
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def submit(self, request, params={}):
        if not self.input_validation():
            obj = self.form_to_model(Physician())
            self.get_service().save(obj)
            self.form['message'] = "Data saved successfully"
        return render(request, self.get_template(), {'form': self.form})

    def get_template(self):
        return "Physician.html"

    def get_service(self):
        return PhysicianService()
