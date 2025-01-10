from django.shortcuts import render,redirect
from ..ctl.BaseCtl import BaseCtl
from ..models import Attribute
from ..Service.AttributeService import AttributeService
from ..utility.DataValidator import DataValidator


class AttributeCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['display'] = requestForm['display']
        self.form['datatype'] = requestForm['datatype']
        self.form['isActive'] = requestForm['isActive']
        self.form['description'] = requestForm['description']

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.display = self.form['display']
        obj.datatype = self.form['datatype']
        obj.isActive = self.form['isActive']
        obj.description = self.form['description']
        return obj

    def model_to_form(self, obj):
        if obj is None:
            return
        self.form['display'] = obj.display
        self.form['datatype'] = obj.datatype
        self.form['isActive'] = obj.isActive
        self.form['description'] = obj.description

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['display'])):
            inputError['display'] = "Display is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['display'])):
                inputError['display'] = "Name only contain Letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['datatype'])):
            inputError['datatype'] = "DataType is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['datatype'])):
                inputError['datatype'] = "Name only contain Letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['isActive'])):
            inputError['isActive'] = "IsActive is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['isActive'])):
                inputError['isActive'] = "Name only contain Letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['description'])):
            inputError['description'] = "Description is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['description'])):
                inputError['description'] = "Description only contain Letters"
                self.form['error'] = True

        return self.form['error']

    def display(self, request, params={}):
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def submit(self, request, params={}):
        r = self.form_to_model(Attribute())
        self.get_service().save(r)
        self.form['message'] = "Data saved Successfully"
        res = render(request, self.get_template(), {'form': self.form})
        return res


    def get_template(self):
        return "Attribute.html"

    def get_service(self):
        return AttributeService()
