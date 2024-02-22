#Write a Python program to remove an empty tuple(s) from a list of tuples

tuple_list = [(1, 2), (), (3, 4), (), (), (5, 6, 7), ()]

non_empty_tuples = []
for tup in tuple_list:
    if tup:
        non_empty_tuples.append(tup)

print("List after removing empty tuples:", non_empty_tuples)