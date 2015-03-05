# Classifier.py
# Class to take data and return a stage of life of the customer

# TODO: change alert that doesn't know about life status?

from __future__ import print_function
import logging
from parse import *
from datetime import date

logging.basicConfig(filename='handler.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

k_STUDENT=-1.0
k_FULL_TIME=1.0

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

        
        try:
            # These classifications require checking previous records.
            name_class = self.get_name_classification(person.get('firstName'), dbData.get('firstName'))
            surname_class = self.get_surname_classification(person.get('lastName'), dbData.get('lastName'))
            location_class = self.get_location_classification(person.get('location'), dbData.get('location'))

            # These classifications work even if it's the first time the customer 
            # is encountered, although they work better with the DB info.
            industry_class = self.get_industry_classification(person.get('industry'), dbData.get('industry'))
            position_class = self.get_position_classification(person.get('positions'), dbData.get('positions'))
            connections_class = self.get_connections_classification(person.get('connections'), dbData.get('connections'))
            headline_class = self.get_headline_classification(person.get('headline'), dbData.get('headline'))

        # except dbdata being none here?
        except TypeError:
            pass

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
        """ If the name has a professional title, they are full-time. """
        professional_titles = ["dr"]
        for title in professional_titles:
            if title in myName.lower():
                return (k_FULL_TIME, 1.0)

        return (k_STUDENT, 0.1)

    def get_surname_classification(self, mySurname, oldSurname):
        """ If the surname has changed, they are working. """
        
        if mySurname is not None and oldSurname is not None:
            if not mySurname == oldSurname:
                return (k_FULL_TIME, 1.0)

        return (k_STUDENT, 0.01)

    def get_location_classification(self, myLocation, oldLocation):
        """ If the location has chnanged, they are working. """
        if myLocation is not None and oldLocation is not None:
            if not myLocation == oldLocation:
                return (k_FULL_TIME, 1.0)
        
        return (k_STUDENT, 0.01)

    def get_industry_classification(self, myIndustry, oldIndustry):
        # TODO: How does industry change things?
        return (0,0)

    def get_position_classification(self, myPositions, oldPositions):
        return (0,0)

    def get_connections_classification(self, myConnections, oldConnections):
        
        return (0,0)

    def get_headline_classification(self, myHeadline, oldHeadline):
        if "student" in myHeadline.lower():
            return (k_STUDENT, 1.0)
        return (0,0)

    def get_dob_classification(self, dob):
        """ If they are under 21, they are a student with 90% confidence.
        If they are 24, they are a student with 50% confidence.
        If they are under 26, they are full-time with 50% confidence.
        If they are above 26, they are full-time with 90% confidence. """
        parsed = parse("{month:d}/{day:d}/{year:d}", dob)
        birthdate = date(parsed['year'], parsed['month'], parsed['day'])
        age = date.today() - birthdate

        if age.days <= 21*365:
            return (k_STUDENT, 0.9)
        if age.days <= 24*365:
            return (k_STUDENT, 0.5)
        if age.days <= 26*365:
            return (k_FULL_TIME, 0.5)

        return (k_FULL_TIME,0.9)

    def combine_classifiers(self, name, surname, location, industry,
        position, connections, headline, dob, weights):
        """ Uses weights to combine classifiers according to their confidence.
        Assumes each classification is a tuple of (classification, confidence). """
        val = (weights.get('name')*name[0]*name[1] + 
            weights.get('surname')*surname[0]*surname[1] + 
            weights.get('location')*location[0]*location[1] +
            weights.get('industry')*industry[0]*industry[1] + 
            weights.get('position')*position[0]*position[1] + 
            weights.get('connections')*connections[0]*connections[1] + 
            weights.get('headline')*headline[0]*headline[1] + 
            weights.get('dob')*dob[0]*dob[1])

        if val > 0:
            return "WORKING"
        else:
            return "STUDENT"