from django.shortcuts import render
from ..Service.MedicationService import MedicationService
from ..ctl.BaseCtl import BaseCtl
from ..models import Medication
from ..utility.DataValidator import DataValidator
from ..utility.HtmlUtility import HTMLUtility


class MedicationCtl(BaseCtl):

    def preload(self, request, params):
        self.form["illness"] = request.POST.get('illness', '')

        if (params['id'] > 0):
            obj = self.get_service().get(params['id'])
            self.form["illness"] = obj.illness

        self.static_preload = {"Yes": "Yes", "No": "No"}

        self.form["preload"]["illness"] = HTMLUtility.get_list_from_dict(
            'illness',
            self.form["illness"],
            self.static_preload
        )

    def request_to_form(self, requestForm):

        self.form['id'] = requestForm['id']
        self.form['fullName'] = requestForm['fullName']
        self.form['illness'] = requestForm['illness']
        self.form['prescriptionDate'] = requestForm['prescriptionDate']
        self.form['dosage'] = requestForm['dosage']

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk

        obj.fullName = self.form['fullName']
        obj.illness = self.form['illness']
        obj.prescriptionDate = self.form['prescriptionDate']
        obj.dosage = self.form['dosage']
        return obj

    def model_to_form(self, obj):
        if obj is None:
            return

        self.form['id'] = obj.id
        self.form['fullName'] = obj.fullName
        self.form['illness'] = obj.illness
        self.form['prescriptionDate'] = obj.prescriptionDate
        self.form['dosage'] = obj.dosage

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

        if (DataValidator.isNull(self.form['illness'])):
            inputError['illness'] = "illness is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['illness'])):
                inputError['illness'] = "illness only contain Letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['prescriptionDate'])):
            inputError['prescriptionDate'] = "prescriptionDate is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isDate(self.form['prescriptionDate'])):
                inputError['prescriptionDate'] = "prescriptionDate is  only YYYY-MM-DD"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['dosage'])):
            inputError['dosage'] = "dosage is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isDosage(self.form['dosage'])):
                inputError['dosage'] = "dosage only contain Letters"
                self.form['error'] = True

        return self.form['error']

    def display(self, request, params={}):
        if (params['id'] > 0):
            obj = self.get_service().get(params['id'])
            self.model_to_form(obj)
        res = render(request, self.get_template(), {'form': self.form})
        return res


    def submit(self, request, params={}):
        r = self.form_to_model(Medication())
        self.get_service().save(r)
        self.form['message'] = "Data saved successfully"
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def get_template(self):
        return "Medication.html"

    def get_service(self):
        return MedicationService()
