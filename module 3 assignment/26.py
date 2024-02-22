# Write a Python script to sort (ascending and descending) a dictionary by value. 

my_dict = {'a': 5, 'b': 2, 'c': 10, 'd': 1, 'e': 7}

sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))

sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Sorted Dictionary (Ascending):", sorted_dict_asc)
print("Sorted Dictionary (Descending):", sorted_dict_desc)