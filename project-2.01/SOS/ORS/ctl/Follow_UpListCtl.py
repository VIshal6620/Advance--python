from django.shortcuts import render
from ..Service.Follow_UpService import Follow_UpService
from ..ctl.BaseCtl import BaseCtl
from ..models import Follow_Up


class Follow_UpListCtl(BaseCtl):
    count = 1

    def request_to_form(self, requestForm):
        self.form['client'] = requestForm.get("client", None)
        self.form['physician'] = requestForm.get("physician", None)
        self.form['appointmentDate'] = requestForm.get("appointmentDate", None)
        self.form['charges'] = requestForm.get("charges", None)
        self.form['ids'] = requestForm.getlist('ids', None)

    def display(self, request, params={}):
        Follow_UpListCtl.count = self.form['pageNo']
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        res = render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})
        return res

    def next(self, request, params={}):
        Follow_UpListCtl.count += 1
        self.form['pageNo'] = Follow_UpListCtl.count
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        self.form['lastId'] = Follow_Up.objects.last().id
        res = render(request, self.get_template(), {"pageList": self.page_list, "form": self.form})
        return res

    def previous(self, request, params={}):
        Follow_UpListCtl.count -= 1
        self.form['pageNo'] = Follow_UpListCtl.count
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        self.form['lastId'] = Follow_Up.objects.last().id
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
                    self.form['message'] = "Data has been deleted successfully"
                else:
                    self.form['error'] = True
                    self.form['message'] = "Data was not deleted"

        self.form['pageNo'] = 1
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        return render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})

    def submit(self, request, params={}):
        Follow_UpListCtl.count = 1
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        if self.page_list == []:
            self.form['message'] = "No record found"
        res = render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})
        return res

    def get_template(self):
        return "Follow_UpList.html"

    def get_service(self):
        return Follow_UpService()
