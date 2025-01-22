from django.shortcuts import render
from ..ctl.BaseCtl import BaseCtl
from ..utility.DataValidator import DataValidator
from ..utility.HtmlUtility import HTMLUtility
from ..Service.InitiativeService import InitiativeService
from ..models import Initiative


class InitiativeCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id', 0)
        self.form['initiativeName'] = requestForm.get('initiativeName', '')
        self.form['type'] = requestForm.get('type', '')
        self.form['startDate'] = requestForm.get('startDate', '')
        self.form['version'] = requestForm.get('version', '')

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.initiativeName = self.form['initiativeName']
        obj.type = self.form['type']
        obj.startDate = self.form['startDate']
        obj.version = self.form['version']

    def model_to_form(self, obj):
        if obj is None:
            return
        self.form['id'] = obj.id
        self.form['initiativeName'] = obj.initiativeName
        self.form['type'] = obj.type
        self.form['startDate'] = obj.startDate
        self.form['version'] = obj.version

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if DataValidator.isNull(self.form['initiativeName']):
            inputError['initiativeName'] = "Initiative Name is required."
            self.form['error'] = True
        else:
            if DataValidator.isalphacehck(self.form['initiativeName']):
                inputError['initiativeName'] = "Initiative Name must contain only letters."
                self.form['error'] = True

        if DataValidator.isNull(self.form['type']):
            inputError['type'] = "Type is required."
            self.form['error'] = True
        else:
            if DataValidator.isalphacehck(self.form['type']):
                inputError['type'] = "Type must contain only letters."
                self.form['error'] = True

        if DataValidator.isNull(self.form["startDate"]):
            inputError["startDate"] = "Start Date is required."
            self.form["error"] = True
        # else:
        #     if DataValidator.isalphacehck(self.form["startDate"]):
        #         inputError["startDate"] = "Start Date YYYY-MM-DD."
        #         self.form["error"] = True

        if DataValidator.isNull(self.form['version']):
            inputError['version'] = "Version is required."
            self.form['error'] = True
        # else:
        #     if DataValidator.isalphacehck(self.form['version']):
        #         inputError['version'] = "version  only contain Letters"
        #         self.form['error'] = True

        return self.form['error']

    def display(self, request, params={}):
        if (params['id'] > 0):
            obj = self.get_service().get(params['id'])
            self.model_to_form(obj)
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def submit(self, request, params={}):
        # Map request data to the form
        self.request_to_form(request.POST)

        # Validate input data
        if self.input_validation():
            # If validation fails, return the form with error messages
            return render(request, self.get_template(), {'form': self.form})

        # Create or update the Initiative model instance
        initiative_obj = Initiative()
        self.form_to_model(initiative_obj)

        # Save the model instance using the service
        self.get_service().save(initiative_obj)

        # Update the form with the saved instance's ID
        self.form['id'] = initiative_obj.id

        # Set success message
        self.form['error'] = False
        self.form['message'] = "Data submitted successfully."

        # Return the updated form
        return render(request, self.get_template(), {'form': self.form})

    def get_template(self):
        return "Initiative.html"

    def get_service(self):
        return InitiativeService()
