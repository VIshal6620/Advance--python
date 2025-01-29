from django.db import connection
from ..Service.BaseService import BaseService
from ..models import Physician
from ..utility.DataValidator import DataValidator


class PhysicianService(BaseService):

    def search(self, params):
        pageNO = (params["pageNo"] - 1) * self.pageSize
        sql = "select* from sos_physician where 1=1"
        val = params.get("display", None)
        if DataValidator.isNotNull(val):
            sql += "and fullName like '" + val + "%%'"
        sql += " limit %s,%s"
        cursor = connection.cursor()
        print("---------", sql, pageNO, self.pageSize)
        cursor.execute(sql, [pageNO, self.pageSize])
        result = cursor.fetchall()
        columnName = ("id", "fullName", "birthDate", "phone", "specialization")
        res = {
            "data": [],
        }
        res["index"] = ((params['pageNo'] - 1) * self.pageSize) + 1
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res['data'].append({columnName[i]: x[i] for i, _ in enumerate(x)})
            return res

    def get_model(self):
        return Physician
