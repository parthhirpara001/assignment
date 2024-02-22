#Write a Python program to split a list into different variables

my_list2 = [5, 6, 7, 4, 3]
variables2 = []

for item in my_list2:
    variables2.append(item)

for i, var in enumerate(variables2, 1):
    print(f"var{i}: {var}")