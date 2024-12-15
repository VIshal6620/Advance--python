import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
cursor = connection.cursor()
sql = "update dept set dep ='abc' where id = 1"
cursor.execute(sql)
connection.commit()
connection.close()
print('data update successfully')
