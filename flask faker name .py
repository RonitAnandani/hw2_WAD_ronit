from distutils.log import debug
from http import client
from flask import Flask, render_template, url_for, request, redirect


import pymongo
from pymongo import MongoClient
import random, time

client = MongoClient('localhost', 27017)
db =client.dataase
app = Flask(__name__)

"""app.config["MONGO_URI"] = "mogodb://localhost:27017/dataase"
mongo = PyMongo(app)
"""
@app.route('/')
def index():
    users = db.users.find({})
    return render_template('login.html', users = users)


@app.route('/age/<int:age>')
def age(age):
    users = db.users.find({"age": age})
    return render_template('login.html', users = users)


if __name__ == "__main__":
    db.users.drop()
    import faker
    from faker import Faker
    faker = Faker()
    db.users.insert_many([{"username": faker.name(), "age": random.randint(10, 25)} for _ in range(10)])
    app.run(host='localhost', port=5001, debug=True)                





""""
def create_01():
    for i in range(1000):
        username = random.randint(0, 10)
        password = random.randint(0, 100)
        db.user.insert_one({
            "username": username,
            "password": password
        })

def create_02():
    users =[]
    for i in range(1000):
        username = random.randint(0, 10)
        password = random.randint(0, 100)
        users.append({"username":username, "password":password})

    db.users.insert_many(users)

t=time.time()
#create_01
create_02
print(f"Operation time = {time.time() - t}")


#mydb=client["mydb"]
#mycol=mydb["people"]
#data = {'name': 'jhonYY', 'age':30}
#mycol.insert_one(data)



#app = Flask(__name__)



@app.route('/')

def login():
    return render_template('login.html')  


#@app.route('/profile')
#def contact():
   # return render_template('contact.html') 

#@app.route('/home')
#def home():
   # return render_template('home.html')

#@app.route('/register')
#def register():
 #   return render_template('register.html') 
    


#if __name__ == "__main__":
 #   app.run(debug=True)  """