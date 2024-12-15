import pymysql

from crud.testread import result


def testread():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    sql = "select * from dept"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(type(result))
    for data in result:
        print(data[0], '\t', data[2])
    connection.commit()
    connection.close()


def testRead2(data):
    name = data.get('id', '')
    rollNo = data.get('dep', 0)
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    sql = "select * from dept"
    if id != '':
        sql += " where id = '" + id + "'"
    if rollNo != 0:
        sql += " where  = " + dep
        str(dep)
    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1])
    connection.commit()
    connection.close()
