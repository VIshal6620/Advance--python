import pymysql


# Function to insert specific values directly
def testInsert1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    sql = "INSERT INTO dept (id, dep) VALUES (6, hello)"
    cursor.execute(sql)
    connection.commit()
    connection.close()


print("Data inserted successfully in testInsert1")


# Function to insert using parameters
def testInsert2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    sql = "INSERT INTO dept (id, dep) VALUES (%s, %s)"
    data = (7, 'Marketing')  # Changed id to 7 to avoid duplication
    cursor.execute(sql, data)
    connection.commit()
    connection.close()


print("Data inserted successfully in testInsert2")


# Function to insert specific values directly with different data
def testinsert3(id, dep):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    sql = "INSERT INTO dept (id, dep) VALUES (7, 'aniket')"
    cursor.execute(sql)
    connection.commit()
    connection.close()


print("Data inserted successfully in testInsert3")


def testInsert4(data):
    id = data['id']
    dep = data['dep']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    sql = "insert into dept values(%s,%s)"
    data = (id, dep)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()


print('data insert successfully')

vishal = {}
vishal['id'] = 6
vishal['dep'] = 'sale'
testInsert4(vishal)
