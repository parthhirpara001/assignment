# Write a Python program to map two lists into a dictionary


keys = ['a', 'b', 'c']
values = [1, 2, 3]



dict1={}
dict2={}

for i in range(len(keys)):
    dict1[keys[i]] = values[i]

print(dict1)