from django.shortcuts import render
from ..Service.CustomerService import CustomerService
from ..ctl.BaseCtl import BaseCtl
from ..models import Customer
from ..utility.DataValidator import DataValidator
from ..utility.HtmlUtility import HTMLUtility


class CustomerCtl(BaseCtl):

    def preload(self, request, params={}):

        self.form['importance'] = request.POST.get('importance', '')

        if (params['id'] > 0):
            obj = self.get_service().get(params['id'])
            self.form['importance'] = obj.importance

        self.static_preload = {"High": "High", "Medium": "Medium", "Low": "Low"}

        self.form['preload']['importance'] = HTMLUtility.get_list_from_dict(
            'importance',
            self.form['importance'],
            self.static_preload
        )

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['clientName'] = requestForm['clientName']
        self.form['location'] = requestForm['location']
        self.form['contactNumber'] = requestForm['contactNumber']
        self.form['importance'] = requestForm['importance']

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.clientName = self.form['clientName']
        obj.location = self.form['location']
        obj.contactNumber = self.form['contactNumber']
        obj.importance = self.form['importance']
        return obj

    def model_to_form(self, obj):
        if obj is None:
            return

        self.form['id'] = obj.id
        self.form['clientName'] = obj.clientName
        self.form['location'] = obj.location
        self.form['contactNumber'] = obj.contactNumber
        self.form['importance'] = obj.importance

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['clientName'])):
            inputError['clientName'] = "clientName is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['clientName'])):
                inputError['clientName'] = "clientName is contain"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['location'])):
            inputError['location'] = "location is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['location'])):
                inputError['location'] = "location is current position"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['contactNumber'])):
            inputError['contactNumber'] = "contactNumber is Required"
            self.form['error'] = True
        else:
            if (DataValidator.ismobilecheck(self.form['contactNumber'])):
                inputError['contactNumber'] = "contactNumber is mobile number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['importance'])):
            inputError['importance'] = "importance is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['importance'])):
                inputError['importance'] = "importance is contain"
                self.form['error'] = True

        return self.form['error']

    def display(self, request, params={}):
        if (params['id'] > 0):
            obj = self.get_service().get(params['id'])
            self.model_to_form(obj)
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def submit(self, request, params={}):
        r = self.form_to_model(Customer())
        self.get_service().save(r)
        self.form['message'] = "Data saved successfully"
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def get_template(self):
        return "Customer.html"

    def get_service(self):
        return CustomerService()
