import pymysql


def testupdate1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    sql = "update dept set dep = 'purches'  where id = 4"
    cursor.execute(sql)
    connection.commit()
    connection.close()


print('Data update successfully')

def testupdate2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    sql = "update dept set dep = %s where id =%s"
    data = ('Hr', 5)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()


print('Data update2')


# testupdate2()


def testupdate3(dep, id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    sql = "update dept set dep =%s where id = %s"
    data = (dep, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()

    print('data update')


# testupdate3('yash' ,5)

def testupdate4(data):
    id = data['id']
    dep = data['dep']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    sql = "update dept set dep = %s where id = %s"
    data = (dep, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()

    print('data update 4 successfully')


vishal = {}
vishal['id'] = 1
vishal['dep'] = 'ncs'
testupdate4(vishal)
