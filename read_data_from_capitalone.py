# function: read_capitalone_data()
#    input: a txt file from Capital One with the basic customers info:
#           id, URL of a customers' LinkedIn personal page
#	        last name, first name, and DOB				
#   output: a list of dictionaries where each dictionary contains fields
#			which represents a customer's basic info
#
def read_capitalone_data():
	list_of_customers = []
	datafile = open('customer_info_capital_one.txt', 'r')
	list_of_data_from_datafile = datafile.readlines()
	for i in range (len(list_of_data_from_datafile)):
		single_line = list_of_data_from_datafile[i]
		single_line_split = single_line.split()
		one_customer_info = {'id': single_line_split[0],
						 'URL': single_line_split[1], 
						 'last name': single_line_split[2], 
						 'first name': single_line_split[3],
						 'dob': single_line_split[4] }
		list_of_customers.append(one_customer_info)
	return list_of_customers

