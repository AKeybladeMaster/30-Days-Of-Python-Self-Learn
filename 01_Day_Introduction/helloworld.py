# Introduction
# Day 1 - 30DaysOfPython Challenge

print("Hello World!")   # print hello world

print(2 + 3)   # addition(+)
print(3 - 1)   # subtraction(-)
print(2 * 3)   # multiplication(*)
print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Beasty'))            # String
print(type([1, 2, 3]))           # List
print(type({'name': 'Beasty'}))  # Dictionary
print(type({9.8, 3.14, 2.7}))    # Tuple

# Euclidean distance

pointA = (2, 3)
pointB = (10, 8)

distance = ((pointB[0] - pointA[0]) ** 2 + (pointB[1] - pointA[1]) ** 2) ** 0.5

print("Euclidean distance between pointA and pointB is:", distance)