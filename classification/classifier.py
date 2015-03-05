# Classifier.py
# Class to take data and return a stage of life of the customer


from __future__ import print_function
import logging
logging.basicConfig(filename='handler.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Start with assumption of student/not student by DOB
# Position history to see new jobs
# Connection analysis
# Location change
# Industry change
# Surname change

k_STUDENT=-1
k_FULL_TIME=1

def print_not_implemented():
    print("{0:s} not implemented".format(__name__))

class Classifier:
    def classify(self, person, dbData=None):
        """ Returns the stage of life of the customer.
        Input: 
            person - a dict with optional string fields
                'firstName',
                'lastName',
                'dob'
                'location',
                'industry', 
                'headline', 
                'positions', 
                'maiden-name', 
                'picture-url'
            dbData - a dict of old data on the person, 
                optional string fields same as those of person

        Returns:
            Stage of Life = (Student | Full-time Employee)
        """

        logging.info("Classifying {0:s} {1:s}".format(person['firstName'], person['lastName']))

        # Because we can't actually train a model (no data), just split the data
        # and make a guess on each feature with some confidence.
        # Then do a linear combination of these guesses.

        # These classifications require checking previous records.
        #if dbData is not None:
        #    name_class = self.get_name_classification(person['firstName'], dbData['firstName'])
        #    surname_class = self.get_surname_classification(db_ID, surname)
        #    location_class = self.get_location_classification(db_ID, location)

        # These classifications work even if it's the first time the customer 
        # is encountered (although they work better with the DB.

        #industry_class = self.get_industry_classification(person['industry'], )
        #position_class = self.get_position_classification(db_ID, position_history)
        #connections_class = self.get_connections_classification(db_ID, connections)
        #distance_class = self.get_distance_classification(db_ID, distance)

        # These classifications do not use the database at all.
        #dob_class = self.get_dob_classification(dob)


        return None


    #def classify(self, person, db_ID=None, name=None, surname=None, location=None, 
    #    position_history=None, industry=None, connections=None, 
    #    distance=None, dob=None):




    #    return self.combine_classifiers(
    #        name=name_class, 
    #        surname=surname_class,
    #        location=location_class,
    #        industry=industry_class,
    #        position=position_class,
    #        connections=connections_class,
    #        distance=distance_class,
    #        dob=dob_class,
    #        weights=self.weights)


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