from ..models import Attribute
from ..utility.DataValidator import DataValidator
from .BaseService import BaseService
from django.db import connection


class AttributeService(BaseService):
    #
    # def search(self, params):
    #     pageNo = (params['pageNo'] - 1) * self.pageSize
    #     sql = 'select * from sos_attribute where 1=1'
    #     val = params.get('display', None)
    #     if (DataValidator.isNotNull(val)):
    #         sql += " and display = '" + val + "'"
    #     sql += " limit %s, %s"
    #     cursor = connection.cursor()
    #     cursor.execute(sql, [pageNo, self.pageSize])
    #     result = cursor.fetchall()
    #     columnName = ('id', 'display', 'datatype', 'isActive' 'description')
    #     res = {
    #         "data": [],
    #     }
    #     res["index"] = ((params['pageNo'] - 1) * self.pageSize) + 1
    #     for x in result:
    #         print({columnName[i]: x[i] for i, _ in enumerate(x)})
    #         res['data'].append({columnName[i]: x[i] for i, _ in enumerate(x)})
    #     return res
    #
    # def get_model(self):
    #     return Attribute

    def search(self, params):
        pageNo = (params["pageNo"] - 1) * self.pageSize
        sql = "select * from sos_attribute where 1=1"
        val = params.get("display", None)
        if DataValidator.isNotNull(val):
            sql += " and display like '" + val + "%%'"
        sql += " limit %s, %s"
        cursor = connection.cursor()
        print("--------", sql, pageNo, self.pageSize)
        cursor.execute(sql, [pageNo, self.pageSize])
        result = cursor.fetchall()
        columnName = ("id", "display", "datatype", "isActive", "description")
        res = {
            "data": [],
        }
        res["index"] = ((params['pageNo'] - 1) * self.pageSize) + 1
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res['data'].append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def get_model(self):
        return Attribute
