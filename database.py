__author__ = 'Yermek Issatayev'

import pymongo

class Database:
    # Connection to MongoDB when an instance of
    # Database class is created. Basically, it is setupDB()
    # For now, I have db named mydb, and username : 'superAdm', password: '123'
    def __init__(self, dbName, collName, dbUserName, dbPassword):
        self._connection = None
        self._dbName = dbName
        self._collection = collName
        self._dbUserName = dbUserName
        self._dbPassword = dbPassword

        try:
            self._connection = pymongo.MongoClient('localhost', 27017) #host and port
            self._connection[self._dbName].authenticate(self._dbUserName, self._dbPassword)
        except (pymongo.errors.OperationFailure, pymongo.errors.ConnectionFailure), e:
            print "Could not connect to server: %s" % e


    def getCustomerById(self, custID):
        try:
            return self._connection[self._dbName][self._collection].find_one({"custID": custID})
        except pymongo.errors.OperationFailure, e:
            print "Database getCustomer operation failed: %s" % e

    def updateCustomer(self, **newData):
        try:
            self._connection[self._dbName][self._collection].update(
                {"custID": newData.get('custID')},
                newData,
                upsert=False #if no such document is found, don't create a new document
            )
        except pymongo.errors.OperationFailure, e:
            print "Database updateCustomer operation failed: %s" % e

        '''
        #print self._connection[self._dbName][self._collection].find_one({'custID': newData.get('custID')})
        cursor = self._connection[self._dbName][self._collection].find()

        for i in cursor:
            print i
        '''

    def insertCustomer(self, **data):
        try:
            collection = self._connection[self._dbName][self._collection]
        except pymongo.errors.OperationFailure, e:
            print "Database insertCustomer operation failed: %s" % e

        new_customer = {}

        for key, val in data.items():
            new_customer[key] = val

        #insert new_customer to the database if no such id exists
        collection.update(
            {'custID': new_customer.get('custID')},
            new_customer,
            upsert=True
        )

        '''
        cursor = collection.find()
        for i in cursor:
            print i
        '''

    def closeDB(self):
            self._connection.close()
            #print self._connection
