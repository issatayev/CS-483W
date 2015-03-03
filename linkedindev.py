from linkedin import linkedin

class linkedinApi:
    CONSUMER_KEY = '77il23ybk7gobx' 
    CONSUMER_SECRET = 'fFnsP7fCRhwV8Nst'
    USER_TOKEN = '35ab1da7-4bc7-4ff8-91bf-c21f0acfa010'
    USER_SECRET = '8b461c18-eadb-4f49-9135-76053bb03446'
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
