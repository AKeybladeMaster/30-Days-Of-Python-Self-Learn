# Exercises - Day 12

from random import sample, shuffle, randint
from string import ascii_letters, digits, hexdigits

# === LEVEL 1 ===

# Write a function which generates a six digit/character random_user_id
def random_user_id(length=6): return ''.join(sample(ascii_letters + digits, length))

# Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated
def user_id_gen_by_user(length, count): return [random_user_id(length) for _ in range(count)]

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each)
def rgb_color_gen(): return f'rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)})'

# === LEVEL 2 ===

def list_of_hexa_colors(count=1): return ['#' + ''.join(sample(hexdigits.lower()[:16], 6)) for _ in range(count)]
def list_of_rgb_colors(count=1): return [rgb_color_gen() for _ in range(count)]
def generate_colors(kind, count): return list_of_hexa_colors(count) if kind == 'hexa' else list_of_rgb_colors(count) if kind == 'rgb' else []

# === LEVEL 3 ===

# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(items):
    items = items[:]; shuffle(items); return items

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique
def seven_unique_numbers(): return sample(range(10), 7)

if __name__ == '__main__':
    print('random_user_id:', random_user_id())
    print('user_id_gen_by_user:', user_id_gen_by_user(8, 3))
    print('rgb_color_gen:', rgb_color_gen())
    print('list_of_hexa_colors:', list_of_hexa_colors(3))
    print('list_of_rgb_colors:', list_of_rgb_colors(3))
    print('generate_colors (hexa):', generate_colors('hexa', 3))
    print('shuffle_list:', shuffle_list([1, 2, 3, 4, 5]))
    print('seven_unique_numbers:', seven_unique_numbers())
