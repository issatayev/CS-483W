# A class for getting data from LinkedIn profile using linkedin api and python-linkedin library
# This is where Linkedin developer credentials are set up to use the API
from linkedin import linkedin

class linkedinApi:
    # Setting up credentials, should read from a file or authenticate from web in the future
    CONSUMER_KEY = '77x34huvh2z8vr' 
    CONSUMER_SECRET = 'GhmHnUBy1E7fCBlp'
    USER_TOKEN = 'd245c71e-3494-4142-9eb9-8d8d7714c77e'
    USER_SECRET = 'da4a210e-3dde-4b86-808f-13ba51b07b62'
    RETURN_URL = 'http://localhost:8000'
    
    # initialize an instance
    def __init__(self):
        self.authentication = linkedin.LinkedInDeveloperAuthentication(self.CONSUMER_KEY, self.CONSUMER_SECRET,
                                                                        self.USER_TOKEN, self.USER_SECRET,
                                                                        self.RETURN_URL, 
                                                                        linkedin.PERMISSIONS.enums.values())
        self.application = linkedin.LinkedInApplication(self.authentication)

    # returns a dictionary with profile info for the user whose public profile url is given
    def getProfile(self, url):
        return self.application.get_profile(member_url = url, selectors = ['location', 'industry', 'headline', 'positions', 'maiden-name', 'picture-url'])
