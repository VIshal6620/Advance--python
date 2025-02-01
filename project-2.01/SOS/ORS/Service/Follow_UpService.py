from django.db import connection
from ..Service.BaseService import BaseService
from ..models import Follow_Up
from ..utility.DataValidator import DataValidator


class Follow_UpService(BaseService):

    def search(self, params):
        pageNo = (params["pageNo"] - 1) * self.pageSize
        sql = "select * from sos_Follow_Up where 1=1"
        val = params.get("client", None)
        if DataValidator.isNotNull(val):
            sql += " and client like '" + val + "%%'"
        sql += " limit %s, %s"
        cursor = connection.cursor()
        print("--------", sql, pageNo, self.pageSize)
        cursor.execute(sql, [pageNo, self.pageSize])
        result = cursor.fetchall()
        columnName = ("id", "client", "physician", "appointmentDate", "charges")
        res = {
            "data": [],
        }
        res["index"] = ((params['pageNo'] - 1) * self.pageSize) + 1
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res['data'].append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def get_model(self):
        return Follow_Up
