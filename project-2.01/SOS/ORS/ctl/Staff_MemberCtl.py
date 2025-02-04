from MySQLdb.times import format_DATE

from ..ctl.BaseCtl import BaseCtl
from ..utility.HtmlUtility import HTMLUtility


class Staff_MemberCtl(BaseCtl):

    def preload(self, request, params):
        self.form["division"] = request.POST.get('division', '')

        if (params['id'] > 0):
            obj = self.get_service().get(params['id'])
            self.form["division"] = obj.division

        self.static_preload = {"Marketing": "Marketing", "Human Resources": "Human Resources", "Finance": "Finance"}

        self.form["preload"]["division"] = HTMLUtility.get_list_from_dict('division',
                                                                          self.form["division", self.static_preload])

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
