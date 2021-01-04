from flask import Flask, jsonify, request

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
    """
    To create a new store, and to add that store to database containing 
    all the existing stores. 
    """


    request_data = request.get_json() #To get the name of new store
    #get_json automatically converts json to dictionary
    new_store = {
        'name' : request_data['name'], 
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store) #important to jsonify, else will get error.

"""
We tested the get stores method, but we can't test the create store method, 
as it requires quite a complicated JavaScript. However, after implementing all 
the endpoints, we will test them through a professional software, as to 
test the functionality.  
"""


# GET /store/<string:name>
@app.route('/store/<string:name>')
#This is for type of request such as, 'http://127.0.0.1:5000/store/some_name'
#here, the string name has to match the argument of the function
def get_store(name):
    """
    Returns the store data, of a specific store given it exists in the 
    database. If not, gives an error message. 
    """

    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message' : 'Store doesn\'t exist'})


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
    """
    Creates a new item, in an existing store
    """
    

    request_data = request.get_json()
    new_item = {
        'name' : request_data['name'], 
        'price' : request_data['price']
    }
    for store in stores:
        if store['name'] == name:
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'Store not found.'})


#GET /store/<string : name>/items
@app.route('/store/<string:name>/items')
def get_items_in_store(name):
    """
    Returns list of all the items present in the specified store. 
    """


    for store in stores:
        if store['name'] == name:
            return jsonify({'items' : store['items']})
    return jsonify({'message':'Store not found. '})



# GET /store/<string: name>/item_data : {name: }
@app.route('/store/<string:name>/<string:item_name>')
def get_item_in_store(name, item_name):
    """
    Returns a specified item, from a specified store, given both exists. 
    """
    

    for store in stores:
        if store['name'] == name:
            for item in store['items']:
                if item['name'] == item_name:
                    return jsonify(item)
            return jsonify({'message' : 'Item not found. '})
    return jsonify({'message' : 'Store not found. '}) 


"""
Thus, we have created 6 endpoints for our application. But just creating
them isn't useful. We have to implement them. So, how do we implement them? 
First of all, we need something to store details of our stores. 
"""

#As creating a store is difficult, we will start by retriving existing stores.

#After implementing get stores, we will now implement the rest of the endpoints.



app.run(port = 5000)