# Exercises - Day 9

# === LEVEL 1 ===

# If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years
def driving_message(age):
    return 'You are old enough to drive.' if age >= 18 else f'You need {18 - age} more years to learn to drive.'

#  If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b
def compare_numbers(a, b):
    return f'{a} is greater than {b}' if a > b else f'{a} is smaller than {b}' if a < b else f'{a} is equal to {b}'

# === LEVEL 2 ===

# Write a code which gives grade to students according to theirs scores
def grade(score):
    return 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F'

# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer
def season(month):
    months = {'Autumn': ('september', 'october', 'november'), 'Winter': ('december', 'january', 'february'), 'Spring': ('march', 'april', 'may'), 'Summer': ('june', 'july', 'august')}
    return next((name for name, names in months.items() if month.lower() in names), 'Unknown month')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = 'banana'
print('That fruit already exists in the list' if fruit in fruits else fruits + [fruit])
print(driving_message(15), compare_numbers(4, 3), 'Grade assessed:', grade(85), season('October'), '\n')

# === LEVEL 3 ===

# Person dictionary exercises
person = {'first_name': 'Beasty', 'last_name': 'Developer', 'age': 25, 'country': 'Italy', 'is_married': False, 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']}
skills = person.get('skills', [])
print('Skill in thee middle:', skills[len(skills) // 2], '\nDoes he have Python skill?', 'Python' in skills)
if {'React', 'Node', 'MongoDB'} <= set(skills):
    title = 'fullstack developer'
elif {'Node', 'Python', 'MongoDB'} <= set(skills):
    title = 'backend developer'
elif set(skills) == {'JavaScript', 'React'}:
    title = 'front end developer'
else:
    title = 'unknown title'
print('He is a', title)
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")
