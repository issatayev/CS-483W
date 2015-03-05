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

    weights = {'name': 1, 'surname' : 1, 'location' : 1, 'industry' : 1, 
    'position' : 1, 'connections' : 1, 'headline' : 1, 'dob' : 1}

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
        logging.info(person)

        # Because we can't actually train a model (no data), just split the data
        # and make a guess on each feature with some confidence.
        # Then do a linear combination of these guesses.
        name_class = None
        surname_class = None
        location_class = None
        industry_class = None
        position_class = None
        connections_class = None
        headline_class = None
        #distance_class = None
        dob_class = None

        # These classifications require checking previous records.
        if dbData is not None:
            name_class = self.get_name_classification(person.get('firstName'), dbData.get('firstName'))
            surname_class = self.get_surname_classification(person.get('lastName'), dbData.get('lastName'))
            location_class = self.get_location_classification(person.get('location'), dbData.get('location'))

        # These classifications work even if it's the first time the customer 
        # is encountered, although they work better with the DB info.
        industry_class = self.get_industry_classification(person.get('industry'), dbData.get('industry'))
        position_class = self.get_position_classification(person.get('positions'), dbData.get('positions'))
        connections_class = self.get_connections_classification(person.get('connections'), dbData.get('connections'))
        headline_class = self.get_headline_classification(person.get('headline'), dbData.get('headline'))

        # These classifications do not use the database at all.
        dob_class = self.get_dob_classification(person.get('dob'))

        return self.combine_classifiers(
            name=name_class, 
            surname=surname_class,
            location=location_class,
            industry=industry_class,
            position=position_class,
            connections=connections_class,
            headline=headline_class,
            dob=dob_class,
            weights=self.weights)


    def get_name_classification(self, myName, oldName):
        print_not_implemented()
        return None

    def get_surname_classification(self, mySurname, oldSurname):
        print_not_implemented()
        return None

    def get_location_classification(self, myLocation, oldLocation):
        print_not_implemented()
        return None

    def get_industry_classification(self, myIndustry, oldIndustry):
        print_not_implemented()
        return None

    def get_position_classification(self, myPositions, oldPositions):
        print_not_implemented()
        return None

    def get_connections_classification(self, myConnections, oldConnections):
        print_not_implemented()
        return None

    def get_headline_classification(self, myHeadline, oldHeadline):
        print_not_implemented()
        return None

    def get_dob_classification(self, dob):
        print_not_implemented()
        return None

    def combine_classifiers(self, name, surname, location, industry,
        position, connections, headline, dob, weights):
        """ Uses weights to combine classifiers according to their confidence.
        Assumes each classification is a tuple of (classification, confidence). """

        return None
        #return (weights['name']*name[0]*name[1] + 
        #    weights['surname']*surname[0]*surname[1] + 
        #    weights['location']*location[0]*location[1] +
        #    weights['industry']*industry[0]*industry[1] + 
        #    weights['position']*position[0]*position[1] + 
        #    weights['connections']*connections[0]*connections[1] + 
        #    weights['headline']*headline[0]*headline[1] + 
        #    weights['dob']*dob[0]*dob[1])