#Write a Python program to get unique values from a list

my_list = [1,2,3,4,5,6,7,8,9,7,8,9,4,5,6,1,2,3]

unique_list=[]

for i in my_list:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)