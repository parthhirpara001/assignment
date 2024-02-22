# Write a Python program to read last n lines of a file.


file = open('example.txt','r')

n = int(input("Enter no. of last lines you want to read : "))


lines = file.readlines()[-n:]


line = lines[::-1]

for i in line:
    print(i)