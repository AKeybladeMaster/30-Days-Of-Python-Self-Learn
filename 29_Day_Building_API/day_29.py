# Exercises - Day 29

import os, json
from flask import Flask, jsonify, request, Response

def create_app():
    """A small CRUD API. Install Flask, then run this file to start it."""
    app, students = Flask(__name__), {}

    students = [
        {
            'name':'Asabeneh',
            'country':'Finland',
            'city':'Helsinki',
            'skills':['HTML', 'CSS','JavaScript','Python']
        },
        {
            'name':'David',
            'country':'UK',
            'city':'London',
            'skills':['Python','MongoDB']
        },
        {
            'name':'John',
            'country':'Sweden',
            'city':'Stockholm',
            'skills':['Java','C#']
        }
    ]

    @app.get('/api/v1.0/students')
    def all_students(): return Response(json.dumps(students), mimetype='application/json')

    @app.post('/api/v1.0/students')
    def create_student():

        student = request.get_json(force=True)

        # name = request.form['name']
        # country = request.form['country']
        # city = request.form['city']
        # skills = request.form['skills'].split(', ')

        # student = {
        # 'name': name,
        # 'country': country,
        # 'city': city,
        # 'skills': skills
        # }

        # db.students.insert_one(student)

        # student = request.get_json(force=True)
        # student_id = str(len(students) + 1)
        # students[student_id] = {'id': student_id, **student}
        return jsonify('New student added', student), 201

    @app.get('/api/v1.0/students/<student_id>')
    def single_student(student_id):
        return jsonify(students.get(student_id, {'error': 'Student not found'})), 200 if student_id in students else 404

    @app.put('/api/v1.0/students/<student_id>')
    def update_student(student_id):
        if student_id not in students: return jsonify({'error': 'Student not found'}), 404
        students[student_id].update(request.get_json(force=True))
        return jsonify(students[student_id])

    @app.delete('/api/v1.0/students/<student_id>')
    def delete_student(student_id):
        return ('', 204) if students.pop(student_id, None) else (jsonify({'error': 'Student not found'}), 404)
    return app

    # MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
    # client = pymongo.MongoClient(MONGODB_URI)
    # db = client['thirty_days_of_python'] # accessing the database

    # @app.route('/api/v1.0/students/<id>', methods = ['GET'])
    # def single_student_from_db (id):
    #     student = db.students.find({'_id':ObjectId(id)})
    #     return Response(dumps(student), mimetype='application/json')

if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    create_app().run(debug=True, host='0.0.0.0', port=port)

# SKIPPING TOTAL IMPLEMENTATION EXERCISE 