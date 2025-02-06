from django.shortcuts import render
from ..Service.Staff_MemberService import Staff_MemberService
from ..ctl.BaseCtl import BaseCtl
from ..models import Staff_Member


class Staff_MemberListCtl(BaseCtl):
    count = 1

    def request_to_form(self, requestForm):
        self.form['fullName'] = requestForm.get('fullName', None)
        self.form['joiningDate'] = requestForm.get('joiningDate', None)
        self.form['division'] = requestForm.get('division', None)
        self.form['previousEmployer'] = requestForm.get('previousEmployer', None)
        self.form['ids'] = requestForm.getlist('ids', None)

    def display(self, request, params={}):
        Staff_MemberListCtl.count = self.form['pageNo']
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        res = render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})
        return res

    def next(self, request, params={}):
        Staff_MemberListCtl.count += 1
        self.form['pageNo'] = Staff_MemberListCtl.count
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        self.form['lastId'] = Staff_Member.objects.last().id
        res = render(request, self.get_template(), {"pageList": self.page_list, "form": self.form})
        return res

    def previous(self, request, params={}):
        Staff_MemberListCtl.count -= 1
        self.form['pageNo'] = Staff_MemberListCtl.count
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        self.form['lastId'] = Staff_Member.objects.last().id
        res = render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})
        return res


    def deleteRecord(self, request, params={}):
        if not self.form['ids']:
            self.form['error'] = True
            self.form['message'] = "Please select at least one checkbox"
        else:
            for id in self.form['ids']:
                id = int(id)
                record = self.get_service().get(id)
                if record:
                    self.get_service().delete(id)
                    self.form['message'] = "Data delete Successfully"
                else:
                    self.form['error'] = True
                    self.form['message'] = "Data was not delete"

        self.form['pageNo'] = 1
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        return render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})

    def submit(self, request, params={}):
        Staff_MemberListCtl.count = 1
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        if self.page_list == []:
           self.form['message'] = "No record found"
        res = render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})
        return res

    def get_template(self):
        return "Staff_MemberList.html"

    def get_service(self):
        return Staff_MemberService()
