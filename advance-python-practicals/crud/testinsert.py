import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
cursor = connection.cursor()
sql = "insert into dept values(1,'sales')"
cursor.execute(sql)
connection.commit()
connection.close()

print('data inserted successfully')
