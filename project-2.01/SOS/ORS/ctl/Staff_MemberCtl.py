from django.shortcuts import render
from ..Service.Staff_MemberService import Staff_MemberService
from ..ctl.BaseCtl import BaseCtl
from ..models import Staff_Member
from ..utility.DataValidator import DataValidator
from ..utility.HtmlUtility import HTMLUtility


class Staff_MemberCtl(BaseCtl):

    def preload(self, request, params):
        self.form["division"] = request.POST.get('division', '')

        if (params['id'] > 0):
            obj = self.get_service().get(params['id'])
            self.form["division"] = obj.division

        self.static_preload = {"Marketing": "Marketing", "HR": "HR", "IT": "IT"}

        self.form["preload"]["division"] = HTMLUtility.get_list_from_dict('division',
        self.form['division'],
        self.static_preload
                                                                          )

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['fullName'] = requestForm['fullName']
        self.form['joiningDate'] = requestForm['joiningDate']
        self.form['division'] = requestForm['division']
        self.form['previousEmployer'] = requestForm['previousEmployer']

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.fullName = self.form['fullName']
        obj.joiningDate = self.form['joiningDate']
        obj.division = self.form['division']
        obj.previousEmployer = self.form['previousEmployer']
        return obj

    def model_to_form(self, obj):
        if obj is None:
            return

        self.form['id'] = obj.id
        self.form['fullName'] = obj.fullName
        self.form['joiningDate'] = obj.joiningDate
        self.form['division'] = obj.division
        self.form['previousEmployer'] = obj.previousEmployer

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['fullName'])):
            inputError['fullName'] = "fullName is Required"
            self.form['error'] = True
        else:
             if (DataValidator.isalphacehck(self.form['fullName'])):
                inputError['fullName'] = "fullName is Contain"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['joiningDate'])):
            inputError['joiningDate'] = "joiningDate is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isDate(self.form['joiningDate'])):
                inputError['joiningDate'] = "joiningDate is YYYY-MM-DD"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['division'])):
            inputError['division'] = "division is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['division'])):
                inputError['division'] = "division is contain"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['previousEmployer'])):
            inputError['previousEmployer'] = "previousEmployer is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['previousEmployer'])):
                inputError['previousEmployer'] = "previousEmployer is Contain"
                self.form['error'] = True

        return self.form['error']

    def display(self, request, params={}):
        if (params['id'] > 0):
            obj = self.get_service().get(params['id'])
            self.model_to_form(obj)
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def submit(self, request, params={}):
        r = self.form_to_model(Staff_Member())
        self.get_service().save(r)
        self.form['message'] = "Data successfully saved"
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def get_template(self):
        return 'Staff_Member.html'

    def get_service(self):
        return Staff_MemberService()
