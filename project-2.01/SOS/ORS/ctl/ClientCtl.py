from django.shortcuts import render,redirect
from ..models import Client
from ..Service.ClientService import ClientService
from ..ctl.BaseCtl import BaseCtl
from ..utility.DataValidator import DataValidator
from ..utility.HtmlUtility import HTMLUtility
from django.http import HttpResponse


class ClientCtl(BaseCtl):


    def preload(self, request, params):

        self.form["illness"] = request.POST.get('illness', '')


        if (params['id'] > 0):
            obj = self.get_service().get(params['id'])
            self.form["illness"] = obj.illness

        self.static_preload = {"COVID": "COVID", "Stroke": "Stroke","Diabetes": "Diabetes","Allergies":"Allergies","Headaches":"Headaches"}

        self.form["preload"]["illness"] = HTMLUtility.get_list_from_dict(
            'illness',
            self.form["illness"],
            self.static_preload
        )

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['fullName'] = requestForm['fullName']
        self.form['appointmentDate'] = requestForm['appointmentDate']
        self.form['phone'] = requestForm['phone']
        self.form['illness'] = requestForm['illness']


    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.fullName = self.form['fullName']
        obj.appointmentDate = self.form['appointmentDate']
        obj.phone = self.form['phone']
        obj.illness = self.form['illness']
        return obj

    def model_to_form(self, obj):
        if obj is None:
            return
        self.form['id'] = obj.id
        self.form['fullName'] = obj.fullName
        self.form["appointmentDate"] = obj.appointmentDate.strftime("%Y-%m-%d")
        self.form['phone'] = obj.phone
        self.form['illness'] = obj.illness

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['fullName'])):
            inputError['fullName'] = "FullName is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['fullName'])):
                inputError['fullName'] = "FullName is Contain"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['appointmentDate'])):
            inputError['appointmentDate'] = "appointmentDate is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isDate(self.form['appointmentDate'])):
                inputError['appointmentDate'] = "Incorrect Date, should be YYYY-MM-DD"
                self.form['appointmentDate'] = True

        if (DataValidator.isNull(self.form['phone'])):
            inputError['phone'] = "Phone Number is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isphonecheck(self.form['phone'])):
                inputError['phone'] = "Phone Number is Contain"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['illness'])):
            inputError['illness'] = "illness is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['illness'])):
                inputError['illness'] = "illness is Required"
                self.form['error'] = True

        return self.form['error']



    def display(self, request, params={}):
        if (params['id'] > 0):
            obj = self.get_service().get(params['id'])
            self.model_to_form(obj)
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def submit(self, request, params={}):
        r = self.form_to_model(Client())
        self.get_service().save(r)
        self.form['message'] = "Data saved successfully"
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def get_template(self):
        return "Client.html"

    def get_service(self):
        return ClientService()


#
#
#