from django.shortcuts import render
from ..Service.PhysicianService import PhysicianService
from ..ctl.BaseCtl import BaseCtl
from ..models import Physician


class PhysicianListCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['fullName'] = requestForm.get('fullName', None)
        self.form['birthDate'] = requestForm.get('birthDate', None)
        self.form['phone'] = requestForm.get('phone', None)
        self.form['ids'] = requestForm.getlist('ids', None)


    def display(self, request, params={}):
        PhysicianListCtl.count = self.form['pageNo']
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        self.form['lastId'] = Physician.objects.last().id
        res = render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})
        return res

    def next(self, request, params={}):
        PhysicianListCtl.count += 1
        self.form['pageNo'] = PhysicianListCtl.count
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        self.form['lastId'] = Physician.objects.last().id
        res = records(render, self.get_template(), {'pageList': self.page_list, 'form': self.form})
        return res

    def previous(self, request, params={}):
        PhysicianListCtl.count - +1
        self.form['pageNo'] = PhysicianListCtl.count
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        self.form['lastId'] = Physician.objects.last().id
        res = records(render, self.get_template(), {'pageList': self.page_list, 'form': self.form})
        return res

    def deleteRecords(self, request, params={}):
        if not self.form['ids']:
            self.form['error'] = True
            self.form['message'] = "please select at lest one checkbox"
        else:
            for id in self.form['ids']:
                id = int(id)
                records = self.get_service().get(id)
                if records:
                    self.get_service().get(id)
                    self.form['message'] = "Data has been delete successfully"
                else:
                    self.form['error'] = True
                    self.form['message'] = "Data was not delete"

            self.form['pageNo'] = 1
            records = self.get_service().search(self.form)
            self.page_list = records['data']
            self.form['lastId'] = Physician.objects.last().id
            return render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})

    def submit(self, request, params={}):
        PhysicianListCtl.count = 1
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        if self.page_list == []:
            self.form['message'] = "No records found"
        res = render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})
        return res

    def get_template(self):
        return "PhysicianList.html"

    def get_service(self):
        return PhysicianService()
