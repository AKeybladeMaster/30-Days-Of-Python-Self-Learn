
# Single line comment
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

# Multiline String
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# String Concatenation
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name + space + last_name
print(full_name)  # Asabeneh Yetayeh
# Checking length of a string using len() builtin function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name))  # True
print(len(full_name))  # 15

# Unpacking characters
language = 'Python'
a, b, c, d, e, f = language  # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter)  # P
second_letter = language[1]
print(second_letter)  # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # n

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter)  # n
second_last = language[-2]
print(second_last)  # o

# Slicing

language = 'Python'
# starts at zero index and up to 3 but not include 3
first_three = language[0:3]
last_three = language[3:6]
print(last_three)  # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2]
print(pto)  # pto

# Escape sequence
print('I hope every one enjoying the python challenge.\nDo you ?')  # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)')  # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')

# String Methods
# capitalize(): Converts the first character the string to Capital Letter

challenge = 'thirty days of python'
print(challenge.capitalize())  # 'Thirty days of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = 'thirty days of python'
print(challenge.count('y'))  # 3
print(challenge.count('y', 7, 14))  # 1
print(challenge.count('th'))  # 2`

# endswith(): Checks if a string ends with a specified ending

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion'))  # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10))  # 'thirty    days      of        python'

# find(): Returns the index of first occurrence of substring

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0

# format()	formats string into nicer output
first_name = 'Beasty'
last_name = 'Developer'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(
    first_name, last_name, job, country)
print(sentence)  # I am Beasty Developer. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi  # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result)  # The area of circle with 10 is 314.0

# index(): Returns the index of substring
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0

# isalnum(): Checks alphanumeric character

challenge = 'ThirtyDaysPython'
print(challenge.isalnum())  # True

challenge = '30DaysPython'
print(challenge.isalnum())  # True

challenge = 'thirty days of python'
print(challenge.isalnum())  # False

challenge = 'thirty days of python 2026'
print(challenge.isalnum())  # False

# isalpha(): Checks if all characters are alphabets

challenge = 'thirty days of python'
print(challenge.isalpha())  # True
num = '123'
print(num.isalpha())      # False

# isdecimal(): Checks Decimal Characters

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0

# isdigit(): Checks Digit Characters

challenge = 'Thirty'
print(challenge.isdigit())  # False
challenge = '30'
print(challenge.isdigit())   # True

# isdecimal():Checks decimal characters

num = '10'
print(num.isdecimal())  # True
num = '10.5'
print(num.isdecimal())  # False


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier())  # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())  # True


# islower():Checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower())  # True
challenge = 'Thirty days of python'
print(challenge.islower())  # False

# isupper(): returns if all characters are uppercase characters

challenge = 'thirty days of python'
print(challenge.isupper())  # False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())  # True


# isnumeric():Checks numeric characters

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False

# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result)  # 'HTML# CSS# JavaScript# React'

# strip(): Removes both leading and trailing characters

challenge = ' thirty days of python '
print(challenge.strip('y'))  # 5

# replace(): Replaces substring inside

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))  # 'thirty days of coding'

# split():Splits String from Left

challenge = 'thirty days of python'
print(challenge.split())  # ['thirty', 'days', 'of', 'python']

# title(): Returns a Title Cased String

challenge = 'thirty days of python'
print(challenge.title())  # Thirty Days Of Python

# swapcase(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.startswith('thirty'))  # True
challenge = '30 days of python'
print(challenge.startswith('thirty'))  # False


# Exercises - Day 4

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
result = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print('Resulting string is: {}'.format(result))

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
result = 'Coding' + ' ' + 'For' + ' ' + 'All'
print('Resulting string is: {}'.format(result))

company = "Coding For All"
print('Company string: {}, Length: {}, Upper case: {}, Lower case: {}'.format(company, len(company), company.upper(), company.lower()))
print('Capitalized: {}, Titled: {}, Swapcase: {}, First word cut out: {}'.format(company.capitalize(), company.title(), company.swapcase(), company[7:]))
print('Does it contain Coding? {}, Word replaced: {}'.format(company.find('Coding'), company.replace('Coding', 'Python')))

string1 = "Python For Everyone"
string2 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print('String replaced: {}, Base string split: {}, 2nd String split: {}'.format(string1.replace('Everyone', 'All'), string1.split(), string2.split()))
print('Char at index 0 of company string: {}, Last index of string: {}'.format(company[0], len(company)))

# What character is at index 10 in "Coding For All" string
print('Character at index 10 in company string: {}'.format(company[10]))

# Create an acronym or an abbreviation for the name 'Python For Everyone'
acronym = ''.join([word[0] for word in string1.split()])

# Create an acronym or an abbreviation for the name 'Coding For All'
acronym2 = ''.join([word[0] for word in company.split()])

# Use index to determine the position of the first occurrence of C and F in Coding For All
print('Position of the first occurrence of C in company string: {}'.format(company.index('C')))
print('Position of the first occurrence of F in company string: {}'.format(company.index('F')))

# Use rfind to determine the position of the last occurrence of l in Coding For All People
string3 = "Coding For All People"
print('Position of the last occurrence of L in string3: {}'.format(string3.rfind('l')))

# Use index or find to find the position of the first occurrence of the word 'because' and rindex to find
# the last occurrence in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
phrase = "You cannot end a sentence with because because because is a conjunction"
print('Position of the first occurrence (using index) of "because" in phrase string: {}'.format(phrase.index('because')))
print('Position of the last occurrence (using rindex) of "because" in phrase string: {}'.format(phrase.rindex('because')))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('Slice applied in the phrase string: {}'.format(phrase[35:58]))

# Does 'Coding For All' start with a substring Coding?
print('Does "Coding For All" start with "Coding" -> {}'.format(company.startswith("Coding")))

# Does 'Coding For All' end with a substring coding?
print('Does "Coding For All" end with "coding" -> {}'.format(company.endswith("coding")))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string
print('"     Coding For All     " with removed trailing spaces: {}'.format(company.lstrip()))

# Which one of the following variables returns True when we use the method isidentifier(): 
# 1) 30DaysOfPython 
# 2) thirty_days_of_python
print('isidentifier() results on 30DaysOfPython -> {} , thirty_days_of_python -> {}'.format('30DaysOfPython'.isidentifier(), 'thirty_days_of_python'.isidentifier()))

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string
librariesList = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('Libraries list joined by hash with space: {}'.format('# '.join(librariesList)))

# Use the new line escape sequence to separate the following sentences:
# I am enjoying this challenge
# I just wonder what is next
print("I am enjoying this challenge.\nI just wonder what is next.")

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# Use the string formatting method to display the following: 
# radius = 10 
# area = 3.14 * radius ** 2 
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

# Make the following using string formatting methods
a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))