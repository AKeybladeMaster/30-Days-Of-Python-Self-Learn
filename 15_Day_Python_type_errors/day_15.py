# Exercises - Day 15

# Type errors are avoided by checking/converting values before using them.
def add_numbers(first, second):
    try:
        return float(first) + float(second)
    except (TypeError, ValueError):
        return 'Please provide two numeric values.'

print(add_numbers(2, '3'))
print(add_numbers(2, 'three'))
