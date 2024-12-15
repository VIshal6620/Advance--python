from MarksheetModel import MarksheetModel


def testAdd():
    vishal = {}
    vishal['Roll_num'] = 366
    vishal['Name'] = 'Atual'
    vishal['Hindi'] = 66
    vishal['Englsh'] = 55
    vishal['Maths'] = 44

    model = MarksheetModel()
    model.add(vishal)

#testAdd()

def testUpdate():
    vishal = {}
    vishal['id'] = 7
    vishal['Roll_num'] = 666
    vishal['Name'] = 'Ram'
    vishal['Hindi'] = 50
    vishal['Englsh'] = 40
    vishal['Maths'] = 60

    model = MarksheetModel()
    model.update(vishal)

#testUpdate()

def testDelete():
    model = MarksheetModel()
    model.delete(10)

#testDelete()

def testRead():
    model = MarksheetModel()
    model.read()

#testRead()

def testGet():
    model = MarksheetModel()
    model.get(2)

#testGet()

def testFindByRollNo():
    model = MarksheetModel()
    model.fineByRoll(456)

#testFindByRollNo()

def testSearch():
    vishal = {}
    vishal['Name'] = 'abc'
    vishal['Roll_No'] = 101
    vishal['pageNo'] = 1
    vishal['pageSize'] = 0
    model = MarksheetModel()
    model.search(vishal)


# testAdd()
# testUpdate()
# testRead()
# testGet()
# testFindByRollNo()
testSearch()