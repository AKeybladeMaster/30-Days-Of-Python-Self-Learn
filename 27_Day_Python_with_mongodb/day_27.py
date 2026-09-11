# Exercises - Day 27

# The lesson has no separate exercise. This connection helper keeps credentials out of source code.
import os # importing operating system module
from pymongo import MongoClient
from bson.objectid import ObjectId # id object

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database

students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
for student in students:
    db.students.insert_one(student)

student = db.students.find_one()
print(student)

student = db.students.find_one({'_id':ObjectId('5df68a23f106fe2d315bbc8c')})
print(student)

students = db.students.find()
for student in students:
    print(student)

students = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # 0 means not include and 1 means include
for student in students:
    print(student)

query = {
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)

query = {
    "country":"Finland",
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)

query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)

students = db.students.find().sort('name',-1)
for student in students:
    print(student)

query = {'age':250}
new_value = {'$set':{'age':38}}

db.students.update_one(query, new_value)
# lets check the result if the age is modified
for student in db.students.find():
    print(student)

query = {'name':'John'}
db.students.delete_one(query)

for student in db.students.find():
    print(student)

db.students.drop()