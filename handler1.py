from linkedin_api.linkedindev import *
import time
from capital_one_data.read_data_from_capitalone import *
from database.database import *
import classification.classifier as classifier
import logging

def updateData(db):
    try:
        # setting up API
        inApi = linkedinApi()
        # reading data from Capital One file into a list of dictionaries, will store new data
        #data = read_capitalone_data('capital_one_data/customer_info_capital_one.txt') 
        data = db.getAllCustomers()

        # initializing a list of dictionaries for info from DB, stores old data
        #dbData = []                                               

        clf = classifier.Classifier()
        for person in data:
            # getting linkedin profiles
            profileData = inApi.getProfile(person['URL'])
        
            # adding data fields from linkedin profile to the initial customers data 
            newPerson = person.copy()
            newPerson.update(profileData) 
        
            # getting information from DB as a dictionary
            #db_temp = db.getCustomerById(person['id'])     
            # adding to the list of data from DB 
            #dbData.append(db_temp)                        

            #person = data[i]

            # get status
            #status = call clasify with dataList[i] and db_data_list[i] and get some status
            if person['status'] == None:
                status = clf.classify(newPerson)
            else:
                status = clf.classify(newPerson, person)
            #status = 'test3'
            #oldStatus = person['status']
        
            # assign status to the customer in the data list
            newPerson['status'] = status
        
            # check if status has changed
            # trigger alert on any change for now, later only on specific changes
            if person['status'] != newPerson['status']:
                print "Alert for " + person['firstName'] + ": changed to " + str(newPerson['status']) + " from " + str(person['status'])
		newPerson['lastStatusChange'] = time.asctime(time.localtime(time.time())) 
            
	    # update or insert customer in db (status and any changes from linkedin)
            db.updateCustomer(newPerson)

    except Exception as inst:
        print '{}:{}'.format(type(inst), inst) 

logging.basicConfig(filename='handler.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info('Program has started')


logging.info('Setting up API')

logging.info('Setting up DB')
# setting up DB
db = Database('mydb','customers','superAdm','123')

logging.info('Reading file')

updateData(db)
    
db.closeDB()
