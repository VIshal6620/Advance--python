from tkinter.font import names

import pymysql

class MarksheetModel:

    def nextPk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "SELECT MAX(id) FROM marksheet"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def add(self, data):
        id = self.nextPk()
        Roll_num = data['Roll_num']
        Name = data['Name']
        Hindi = data['Hindi']
        Englsh = data['Englsh']
        Maths = data['Maths']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "INSERT INTO marksheet (id, Roll_num, Name, Hindi, Englsh, Maths) VALUES (%s, %s, %s, %s, %s, %s)"
        data_tuple = (id, Roll_num, Name, Hindi, Englsh, Maths)
        cursor.execute(sql, data_tuple)
        connection.commit()
        connection.close()
        print('Data inserted successfully')

    def update(self, data):
        id = data['id']
        Roll_num = data['Roll_num']
        Name = data['Name']
        Hindi = data['Hindi']
        Englsh = data['Englsh']
        Maths = data['Maths']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "UPDATE marksheet SET Roll_num = %s, Name = %s, Hindi = %s, Englsh = %s, Maths = %s WHERE id = %s"
        data_tuple = (Roll_num, Name, Hindi, Englsh, Maths, id)
        cursor.execute(sql, data_tuple)
        connection.commit()
        connection.close()
        print('Data updated successfully')

    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "DELETE FROM marksheet WHERE id = %s"
        data_tuple = (id,)
        cursor.execute(sql, data_tuple)
        connection.commit()
        connection.close()
        print('Data deleted successfully')

    def read(self):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "SELECT * FROM marksheet"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
        connection.commit()
        connection.close()
        print('Data read successfully')

    def get(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "SELECT * FROM marksheet WHERE id = %s"
        data_tuple = (id,)  # Wrap id in a tuple
        cursor.execute(sql, data_tuple)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
        connection.commit()
        connection.close()

    def fineByRoll(self, Roll_num):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "SELECT * FROM marksheet WHERE Roll_num = %s"
        data_tuple = (Roll_num,)
        cursor.execute(sql, data_tuple)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
        connection.commit()
        connection.close()

    def search(self, data):
        name = data.get('Name', '')
        rollNo = data.get('Roll_no', 0)
        pageNo = data.get('pageNo', 0)
        pageSize = data.get('pageSize', 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "SELECT * FROM  marksheet where 1=1"
        if name != '':
            sql += " and name = '" + name + "'"
        if rollNo != 0:
            sql += " and roll_no = " + str(rollNo)
        if (pageSize > 0):
            pageNo = (pageNo - 1) * pageSize
            sql += " limit " + str(pageNo) + ", " + str(pageSize)
        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
        connection.commit()
        connection.close()
