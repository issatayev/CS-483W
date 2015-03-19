# TO DO: add try-catch and check for missing import, for example.

from flask import Flask
from flask import render_template
from database.database import *
from flask import request

app = Flask(__name__)
db = Database('mydb','customers','superAdm','123')

# Define a route for the default URL, which loads the form
@app.route('/')
def list():
    names = db.getAllCustomers()

    return render_template('customers.html', names = names)

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/process/', methods=['POST'])
def process():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    ID = request.form['id']
    url = request.form['url']

    if firstName == '' or lastName == '' or ID == '' or url == '':
        return 'One of the fields in the form was missing'

    person = {'id':ID, 'firstName':firstName,'lastName':lastName,'url':url,'status':''}
    
    if db.getCustomerById(ID) == None:
        db.insertCustomer(person)
    else:
        db.updateCustomer(person)

    return redirect(url_for('list'))

if __name__ == '__main__':
    app.run()
