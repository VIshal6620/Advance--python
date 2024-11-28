from django.db import connection


class UserService:


    def nextPk(self):
        pk = 0
        cursor = connection.cursor()
        sql = "select max(id) from user"
        cursor.execute(sql)
        result = cursor.fetchall()
        connection.close()
        for data in result:
            if data[0] is not None:
             pk = data[0]
        return pk + 1

    def add(self, data):
        first_name = data['first_name']
        last_name = data['last_name']
        login_id = data['login_id']
        password = data['password']
        dob = data['dob']
        address = data['address']

        sql = "insert into user values((%s), (%s), (%s), (%s), (%s), (%s), (%s))"
        data = [UserService.nextPk(self), first_name, last_name, login_id, password, dob, address]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()


    def update(self, data):
        first_name = data['first_name']
        last_name = data['last_name']
        login_id = data['login_id']
        password = data['password']
        dob = data['dob']
        address = data['address']
        id = data['id']
        sql = "update user set first_name = (%s), last_name = (%s), login_id = (%s), password = (%s), dob = (%s), address = (%s) where id = (%s)"
        data = [first_name, last_name, login_id, password, dob, address, id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()


    def delete(self, id):
        sql = "delete from user where id = (%s)"
        data = [id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()


    def auth(self, login_id, password):
        sql = "select * from user where login_id = (%s) and password = (%s)"
        data = [login_id, password]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "first_name", "last_name", "login_id", "password", "dob", "address")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res


    def get(self, id):
        sql = "select * from user where id = (%s)"
        data = [id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "first_name", "last_name", "login_id", "password", "dob", "address")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res


    def findByLogin(self, loginId):
        sql = "select * from user where login_id = (%s)"
        data = [loginId]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "first_name", "last_name", "login_id", "password", "dob", "address")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res


    def search(self, params):
        fname = params.get("first_name", "")
        pageNo = params.get("pageNo", 0)
        pageSize = params.get("pageSize", 0)
        sql = "select * from user where 1=1"
        if fname != "":
            sql += " and first_name like '" + fname + "%%' "
        if (pageSize > 0):
            pageNo = (pageNo - 1) * pageSize
            sql += " limit %s, %s"
        print('sql => ', sql)
        cursor = connection.cursor()
        cursor.execute(sql, [pageNo, pageSize])
        result = cursor.fetchall()
        columnName = ("id", "first_name", "last_name", "login_id", "password", "dob", "address")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res
