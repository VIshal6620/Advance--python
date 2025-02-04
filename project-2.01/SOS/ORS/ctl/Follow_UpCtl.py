from django.shortcuts import render
from ..Service.AttributeService import AttributeService
from ..Service.Follow_UpService import Follow_UpService
from ..ctl.BaseCtl import BaseCtl
from ..models import Follow_Up
from ..utility.DataValidator import DataValidator
from ..utility.HtmlUtility import HTMLUtility


class Follow_UpCtl(BaseCtl):

    def preload(self, request, params):

        # Initialize form dictionary for client and physician
        self.form["client"] = request.POST.get('client', '')
        self.form["physician"] = request.POST.get('physician', '')

        # Fetch existing data if ID is greater than 0
        if params.get('id', 0) > 0:
            obj = self.get_service().get(params['id'])
            self.form["client"] = obj.client
            self.form["physician"] = obj.physician  # Reusing the same object

        # Static preload data for clients and physicians
        self.static_client_preload = {
            "John Doe": "John Doe",
            "Michael Johnson": "Michael Johnson"
        }

        self.static_physician_preload = {
            "Dr. Vishal": "Dr. Vishal",
            "Dr. Smith": "Dr. Smith"
        }

        # Initialize preload dictionary
        self.form["preload"] = {}

        # Populate dropdown lists separately
        self.form["preload"]["client"] = HTMLUtility.get_list_from_dict(
            'client',
            self.form["client"],
            self.static_client_preload
        )

        self.form["preload"]["physician"] = HTMLUtility.get_list_from_dict(
            'physician',
            self.form["physician"],
            self.static_physician_preload
        )


    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['client'] = requestForm['client']
        self.form['physician'] = requestForm['physician']
        self.form['appointmentDate'] = requestForm['appointmentDate']
        self.form['charges'] = requestForm['charges']

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.client = self.form['client']
        obj.physician = self.form['physician']
        obj.appointmentDate = self.form['appointmentDate']
        obj.charges = self.form['charges']
        return obj

    def model_to_form(self, obj):
        if obj is None:
            return
        self.form['id'] = obj.id
        self.form['client'] = obj.client
        self.form['physician'] = obj.physician
        self.form['appointmentDate'] = obj.appointmentDate
        self.form['charges'] = obj.charges

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['client'])):
            inputError['client'] = "client is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['client'])):
                inputError['client'] = "client only contain Letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['physician'])):
            inputError['physician'] = "physician is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isDrName(self.form['physician'])):
                inputError['physician'] = "physician only contain Letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['appointmentDate'])):
            inputError['appointmentDate'] = "appointmentDate is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isAppointmentDate(self.form['appointmentDate'])):
                inputError['appointmentDate'] = "appointmentDate only contain Letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['charges'])):
            inputError['charges'] = "charges is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isInteger(self.form['charges'])):
                inputError['charges'] = "charges only contain Letters"
                self.form['error'] = True

        return self.form['error']

    def display(self, request, params={}):
        if (params['id'] > 0):
            obj = self.get_service().get(params['id'])
            self.model_to_form(obj)
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def submit(self, request, params={}):
        r = self.form_to_model(Follow_Up())
        self.get_service().save(r)
        self.form['message'] = "Data saved successfully"
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def get_template(self):
        return "Follow_Up.html"

    def get_service(self):
        return Follow_UpService()
