# TO DO: add try-catch and check for missing import, for example.

from flask import Flask
from flask import render_template
from database.database import *
from flask import request

app = Flask(__name__)
db = Database('mydb','customers','superAdm','123')

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/process/', methods=['POST'])
def process():
    name=request.form['name']
    ID=request.form['id']
    if db.getCustomerById(ID) == None:
        db.insertCustomer({'id': ID, 'firstName':name, 'status':''})
    else:
        db.updateCustomer({'id': ID, 'firstName':name, 'status':''})

    return render_template('form_action.html', ID=ID, name = name)

# list all data
@app.route('/list/')
def list():
    names = db.getAllCustomers()

    return render_template('customers.html', names = names)

if __name__ == '__main__':
    app.run()
