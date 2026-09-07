# Exercises - Day 5

# === LEVEL 1 ===

# Create an empty tuple
emptyTuple = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothersTuple = ('Riku', 'Sora', 'Goofy', 'Donald')
sistersTuple = ('Kairi', 'Yuffie', 'Aerith')

# Join brothers and sisters tuples and assign it to siblings
siblings = brothersTuple + sistersTuple

# How many siblings do you have?
print('I have this many siblings -> ', len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Mom', 'Dad')
family_members = parents + siblings

# === LEVEL 2 ===

# Unpack siblings and parents from family_members
# DONE ALREADY -> siblings, parents tuples

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('Shampoo', 'Nail clipper', 'Anti-mosquito spray')

food_stuff_tp = fruits + vegetables + animal_products

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = len(food_stuff_tp) // 2

if len(food_stuff_tp) % 2 == 0:
    print(food_stuff_tp[middle - 1:middle + 1])
else:
    print(food_stuff_tp[middle])

# Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

# Delete the food_stuff_tp tuple completely
del food_stuff_tp



