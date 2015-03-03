from linkedindev import *
from read_data_from_capitalone import *
from database import *
# import BenClassifier
import logging

logging.basicConfig(filename='handler.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info('Program has started')


logging.info('Setting up API')
# setting up API
inApi = linkedinApi()

logging.info('Setting up DB')
# setting up DB
db = Database('mydb','customers','superAdm','123')

logging.info('Reading file')

# reading data from Capital One file into a list of dictionaries, will store new data
data = read_capitalone_data('customer_info_capital_one.txt') 

# initializing a list of dictionaries for info from DB, stores old data
dbData = []                                                

for person in data:
    # getting linkedin profiles
    profileData = inApi.getProfile(person['URL'])
    
    # adding data fields from linkedin profile to the initial customers data 
    person.update(profileData) 
    
    # getting information from DB as a dictionary
    db_temp = db.getCustomerById(person['id'])     
    # adding to the list of data from DB 
    dbData.append(db_temp)                        


for i in range(len(data)):
    person = data[i]

    # get status
    #status = call clasify with dataList[i] and db_data_list[i] and get some status
    
    status = 'test3'
    
    # assign status to the customer in the data list
    person['status'] = status
    
    # update or insert customer in db (status and any changes from linkedin)
    if dbData[i] == None:
        db.insertCustomer(person)
        oldStatus = None
    else:
        db.updateCustomer(person)
        oldStatus = dbData[i]['status']
     
    # check if status has changed
    # trigger alert on any change for now, later only on specific changes
    if oldStatus != status:
        print "Alert for " + person['firstName'] + ": changed to " + str(status) + " from " + str(oldStatus)
    
db.closeDB()
