"""Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
Expected Output:
ac ad bc bd """

data = {'1': ['a', 'b'], '2': ['c', 'd']}

keys = list(data.keys())
values = list(data.values())

combinations = ['']
for key in keys:
    temp = []
    for comb in combinations:
        for letter in values[keys.index(key)]:
            temp.append(comb + letter)
    combinations = temp

print("Combinations:")
for combination in combinations:
    print(combination)
