from UserModel import UserModel
import datetime


def testadd():
    vishal = {}
    vishal['first_Name'] = 'jatin'
    vishal['last_Name'] = 'patel'
    vishal['code'] = 10
    vishal['dob'] = datetime.date(2003, 12, 27)
    vishal['city'] = 'Indore'

    model = UserModel()
    model.add(vishal)


# testadd()

def testUpdate():
    vishal = {}
    vishal['id'] = 2
    vishal['first_Name'] = 'Mohit'
    vishal['last_Name'] = 'patidar'
    vishal['code'] = 65
    vishal['dob'] = datetime.date(2004, 6, 2)
    vishal['city'] = 'Delhi'

    model = UserModel()
    model.update(vishal)


# testUpdate()

def testDelete():
    model = UserModel()
    model.delete(3)

# testDelete()

def testRead():
    model = UserModel()
    model.read()

# testRead()

def testGet():
    model = UserModel()
    model.get(2)

# testGet()

def testfindbylogin():
    model = UserModel()
    model.findbylogin(2)

# testfindbylogin()


def testSearch():
    vishal = {}
    vishal['pageNo'] = 1
    vishal['pageSize'] = 4
    model = UserModel()
    model.search(vishal)

    testDelete()
    testadd()
    testUpdate()
    testRead()
    testGet()
    testfindbylogin()
    testSearch()