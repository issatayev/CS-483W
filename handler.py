# import AlibekApi
# import YermekDB
# import BenClassifier
import logging
from read_data_from_capitalone import *

logging.basicConfig(filename='handler.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info('Program has started')

# data from capital one:    id
#                           URL
#                           last name
#                           first name
#                           dob

# data from LinkedIn:       currentPosition []
#                           industry
#                           location
#                           picture-url
#                           maiden-name
#                           headline


logging.info('Setting up API')
# setting up API
# some code here...........

logging.info('Setting up DB')
# setting up DB
# some code here...........

logging.info('Reading file')
dataList = read_capitalone_data('customer_info_capital_one.txt') # reading data from Capital One file into a list of dictionaries. (txt for now)
db_data_list = []                                                # list of dictionaries for info from DB

#for person in dataList:
    #tempDict = some_dictionary_from_LinkedIn(person['URL']) #getting basic profile form LinkedIn as a dictionary
    #db_temp = some_dictionary_from_DB(person['id'])         #getting information from DB as a dictionary
    #person.update(tempDict)                                 #updating dataList with info we got from LinkedIn
    #db_data_list.append(db_temp)                            #creating a list of dictionaries from info we got from DB


#for i in range(len(dataList)):
    #status = call clasify with dataList[i] and db_data_list[i] and get some status

    #for each person check if(status != datalist[i]['status']) ALERT!
    #else push dataList[i] to DB
