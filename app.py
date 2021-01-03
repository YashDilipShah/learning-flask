from flask import Flask

app = Flask(__name__) #name given to the specific app. To identify it

"""Now we will use a decorator to add a custom path to out application
This will allow our app to set the path. 
Initially, the app always starts at the home page ie /
Example : https://www.google.com/ lends to home page of google"""

@app.route('/') #This is an endpoint and leads to homepage
def homepage(): #Name doesn't matter in Flask
    
    return "My first app" #Returns hello world when app is run 

app.run(port = 5000) #running the app in the specific port