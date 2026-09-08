# Exercises - Day 8

# Create an empty dictionary called dog and add its details
# Add name, color, breed, legs, age to the dog dictionary
dog = {}
dog['name'] = 'Rex'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3
print('Dog ->', dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Beasty',
    'last_name': 'Developer',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'Italy',
    'city': 'Milan',
    'address': 'Milan, Italy'
}

# Get the dictionary length, skills, keys, values and items
print('Student dictionary length ->', len(student))
print('Skills ->', student['skills'], '| Type ->', type(student['skills']))

# Add skills to the student dictionary
# Get the dictionary keys as a list
# Get the dictionary values as a list
# Change the dictionary to a list of tuples using items() method
student['skills'].extend(['HTML', 'CSS'])
print('Updated skills ->', student['skills'])
print('Keys ->', list(student.keys()))
print('Values ->', list(student.values()))
print('Items ->', list(student.items()))

# Delete one dictionary item, then delete the dog dictionary
del student['marital_status']
del dog
