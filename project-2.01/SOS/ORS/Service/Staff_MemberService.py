from django.db import connection
from ..Service.BaseService import BaseService
from ..utility.DataValidator import DataValidator


class Staff_MemberService(BaseService):

    def search(self, params):
        pageNo = (params["pageNo"] - 1) * self.pageSize
        sql = "select * from sos_Staff_Member where 1=1"
        val = params.get("display", None)
        if DataValidator.isNotNull(val):
            sql += " and fullName like '" + val + "%%'"
        sql += " limit %s, %s"
        cursor = connection.cursor()
        print("--------", sql, pageNo, self.pageSize)
        cursor.execute(sql, [pageNo, self.pageSize])
        result = cursor.fetchall()
        columnName = ("id", "fullName", "joiningDate", "division", "previousEmployer")
        res = {
            "data": [],
        }
        res["index"] = ((params["page No"] - 1) * self.pageSize) + 1
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res['data'].append({columnName[i]: x[i] for i, _ in enumerate(x)})
            return res

    def get_model(self):
        return Staff_MemberService
