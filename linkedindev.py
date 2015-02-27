from linkedin import linkedin

# returns a dictionary object containing basic profile info for user whose public profile url is given
# also requires linkedin application (dev or user) object  
def get_basic_info(application, url):
    return application.get_profile(member_url = url, selectors = ['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'industry', 'email-address', 'headline', 'positions'])


# Set up for application object
# Probably need to create a separate class or a function to initiate parameters
# and create application object (might just check if application was created with every request,but it's inefficient)

CONSUMER_KEY = '77x34huvh2z8vr' 
CONSUMER_SECRET = 'GhmHnUBy1E7fCBlp'
USER_TOKEN = '899f8135-6c20-40bb-8e0d-601751d6ce2f'
USER_SECRET = '76e88455-ba62-4a51-b59b-9dd6f04aeee4'
RETURN_URL = 'http://localhost:8000'

# Instantiate the developer authentication class object

authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                                          USER_TOKEN, USER_SECRET, 
                                                          RETURN_URL, linkedin.PERMISSIONS.enums.values())

# Create an application object (static field of a global class would be better ...)

application = linkedin.LinkedInApplication(authentication)


url = 'https://www.linkedin.com/pub/yermek-issatayev/61/927/800'

# Pass the app to the function
data =  get_basic_info(application, url)

name = data['firstName']

print 'Here is some publicly available info about ' + name + ': ' + str(data)
