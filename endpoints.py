from flask import Flask, jsonify 

app = Flask(__name__)

stores = [
    {
        'name' : 'My wonderful store', 
        'items': [
            {
                'name' : 'My Item',
                'price' : 15.99
            }
        ]
    }
]
"""
Thus, in our stores list, it is actually a list of dictionaries. 
Inside each dictionary, we have name of store, and list of items. 
Every element inside the list of items, is a disctionary, which contains
name and price of that particular product. 

GENERALLY, this kind of data is stored in database, but to simplify things, 
right now we will store them as a data structure. 
"""

# Terminology from server's perspective
# POST : Used to receive the data
# GET : used to Send the data back only

"""What we will implement in this app"""


# POST /store data: {name: }
@app.route('/store', methods=['POST']) #By default, it is always GET
def create_store():
    pass


# GET /store/<string:name>
@app.route('/store/<string:name>')
#This is for type of request such as, 'http://127.0.0.1:5000/store/some_name'
#here, the string name has to match the argument of the function
def get_store(name):
    pass


# GET /store
@app.route('/store')
def get_stores():

    #Returns json like version of stores dictionary. Info in notes. 

    """
    One implementation note: jsonify, only takes dictionaries as input
    but our stores is a list. Thus, we will have to pass a dictionary to 
    jsonify. 
    """

    return jsonify({'stores' : stores})


# POST /store/<string: name>/item {name:, price: }
@app.route('/store/<string:name>/item', methods=["POST"])
def create_item_in_store(name):
    pass


# GET /store/<string: name>/
@app.route('/store/<string:name>')
def get_item_in_store(name):
    pass


"""
Thus, we have created 5 endpoints for our application. But just creating
them isn't useful. We have to implement them. So, how do we implement them? 
First of all, we need something to store details of our stores. 
"""

#As creating a store is difficult, we will start by retriving existing stores.


app.run(port = 5000)