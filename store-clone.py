from flask import Flask

app = Flask(__name__)

# Terminology from server's perspective
# POST : Used to receive the data
# GET : used to Send the data back only

"""What we will implement in this app"""
# POST /store data: {name: }
# GET /store/<string:name>
# GET /store
#