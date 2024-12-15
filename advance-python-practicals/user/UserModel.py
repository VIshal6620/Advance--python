import pymysql

class UserModel:

    def nextpk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
        cursor = connection.cursor()
        sql = "select max(id) from user"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def add(self, data):
        id = UserModel.nextpk(self)
        first_Name = data['first_Name']
        last_Name = data['last_Name']
        code = data['code']
        dob = data['dob']
        city = data['city']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
        cursor = connection.cursor()
        sql = "insert into user value(%s,%s,%s,%s,%s,%s)"
        data = (id, first_Name, last_Name, code, dob, city)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    print('data insert successfully')

    def update(self, data):
        id = data['id']
        first_Name = data['first_Name']
        last_Name = data['last_Name']
        code = data['code']
        dob = data['dob']
        city = data['city']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
        cursor = connection.cursor()
        sql = "update user set first_name = %s, last_name = %s, code = %s, dob = %s, city = %s where id = %s"
        data = (first_Name, last_Name, code, dob, city, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data updated successfully')

    def delete(self,id):
        connection =pymysql.connect(host='localhost',port=3306,user='root',password='root',db='user')
        cursor = connection.cursor()
        sql = "delete from user where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')

    def read(self):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
        cursor = connection.cursor()
        sql = "select * from user"
        cursor.execute(sql)
        result = cursor.fetchall()
        columnName = ("id", "first_Name", "last_Name", "code","dob","city")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def get(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
        cursor = connection.cursor()
        sql = "select * from user where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "code","dob","city")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res
    def findbylogin(self, loginId):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
        cursor = connection.cursor()
        sql = "select * from user where id = %s"
        data = (loginId)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "code","dob","city")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def search(self, data):
        firstName = data.get('firstName', '')
        dob = data.get('dob', 0)
        pageNo = data.get('pageNo', 0)
        pageSize = data.get('pageSize', 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
        cursor = connection.cursor()
        sql = "select * from user where 1=1"
        if firstName != '':
            sql += " and first_name='" + firstName + "'"
        if dob != 0:
            sql += " and dob= " + str(dob)
        if (pageSize > 0):
            pageNo = (pageNo - 1) * pageSize
            sql += " limit " + str(pageNo) + ", " + str(pageSize)
        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "code","dob","city")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res
