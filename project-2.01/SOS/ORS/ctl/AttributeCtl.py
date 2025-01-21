from django.shortcuts import render
from ..ctl.BaseCtl import BaseCtl
from ..models import Attribute
from ..Service.AttributeService import AttributeService
from ..utility.DataValidator import DataValidator
from ..utility.HtmlUtility import HTMLUtility


class AttributeCtl(BaseCtl):

    def preload(self, request, params):

        self.form["isActive"] = request.POST.get('isActive', '')


        if (params['id'] > 0):
            obj = self.get_service().get(params['id'])
            self.form["isActive"] = obj.isActive

        self.static_preload = {"Yes": "Yes", "No": "No"}

        self.form["preload"]["isActive"] = HTMLUtility.get_list_from_dict(
            'isActive',
            self.form["isActive"],
            self.static_preload
        )


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
        self.form['id'] = obj.id
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
                inputError['display'] = "display only contain Letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['datatype'])):
            inputError['datatype'] = "Datatype is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['datatype'])):
                inputError['datatype'] = "Datatype only contain Letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['isActive'])):
            inputError['isActive'] = "Display is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['isActive'])):
                inputError['isActive'] = "isActive only contain Letters"
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
        self.form['message'] = "Data saved successfully"
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def get_template(self):
        return "Attribute.html"

    def get_service(self):
        return AttributeService()
