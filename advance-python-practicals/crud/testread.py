import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
cursor = connection.cursor()
sql = "select * from dept"
cursor.execute(sql)
result = cursor.fetchall()
for data in result:
    print(data[0], '\t', data[1])
connection.commit()
connection.close()
