# Classifier.py
# Class to take data and return a stage of life of the customer


from __future__ import print_function

# Start with assumption of student/not student by DOB
# Position History to see new jobs, or if they’re graduating soon
# Connection analysis
# Location change
# Industry change
# Surname change

k_STUDENT=-1
k_FULL_TIME=1

def print_not_implemented():
	print("{0:s} not implemented".format(__name__))

class Classifier:
	def classify(self, db_ID=None, name=None, surname=None, location=None, 
		position_history=None, industry=None, connections=None, 
		distance=None, dob=None):
		""" Returns the stage of life of the customer.
		Assumes input:
		db_ID - String to look up in our DB
		Name - String
		Surname - String
		Location - String
		Position (History) - Array of Object
		Industry - String
		Connections - Array of Object
		(Graph) Distance - Int
		DOB - Date

		Returns:
		Stage of Life = (Student | Full-time Employee) """

		# EACH CLASSIFICATION IS A TUPLE (CLASS, CONFIDENCE)
		# These classifications require checking our database for previous records.
		if db_ID is not None:
			name_class = self.get_name_classification(db_ID, name)
			surname_class = self.get_surname_classification(db_ID, surname)
			location_class = self.get_location_classification(db_ID, location)

		# These classifications work even if it's the first time the customer 
		# is encountered (although they work better with the DB.
		industry_class = self.get_industry_classification(db_ID, industry)
		position_class = self.get_position_classification(db_ID, position_history)
		connections_class = self.get_connections_classification(db_ID, connections)
		distance_class = self.get_distance_classification(db_ID, distance)

		# These classifications do not use the database at all.
		dob_class = self.get_dob_classification(dob)

		return self.combine_classifiers(
			name=name_class, 
			surname=surname_class,
			location=location_class,
			industry=industry_class,
			position=position_class,
			connections=connections_class,
			distance=distance_class,
			dob=dob_class,
			weights=self.weights)


	def get_name_classification(self, db_ID, name):
		print_not_implemented()
		return None

	def get_surname_classification(self, db_ID, surname):
		print_not_implemented()
		return None

	def get_location_classification(self, db_ID, location):
		print_not_implemented()
		return None

	def get_industry_classification(self, db_ID, industry):
		print_not_implemented()
		return None

	def get_position_classification(self, db_ID, position_history):
		print_not_implemented()
		return None

	def get_connections_classification(self, db_ID, connections):
		print_not_implemented()
		return None

	def get_distance_classification(self, db_ID, distance):
		print_not_implemented()
		return None

	def get_dob_classification(self, dob):
		print_not_implemented()
		return None

	def combine_classifiers(self, name, surname, location, 
		position, connections, distance, dob, weights):
		""" Uses weights to combine classifiers according to their confidence """

		return (weights['name']*name[0]*name[1] + 
			weights['surname']*surname[0]*surname[1] + 
			weights['location']*location[0]*location[1] +
			weights['industry']*industry[0]*industry[1] + 
			weights['position']*position[0]*position[1] + 
			weights['connections']*connections[0]*connections[1] + 
			weights['distance']*distance[0]*distance[1] + 
			weights['dob']*distance[0]*distance[1])