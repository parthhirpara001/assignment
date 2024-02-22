# Write a Python program to find the highest 3 values in a dictionary

my_dict = {'a': 10, 'b': 20, 'c': 15, 'd': 5, 'e': 25}

values = list(my_dict.values())

sorted_values = sorted(values, reverse=True)

highest_three = sorted_values[:3]

print("Highest three values:", highest_three)