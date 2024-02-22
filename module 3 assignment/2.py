#Write a Python program to count the number of strings where the string
#length is 2 or more and the first and last character are same from a given
#list of strings. 


def count_strings_with_same_first_and_last_char(string_list):
    count = 0
    for string in string_list:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count


color = ["black", "white", "pink", "yello", "orange", "red", "green"]

result = count_strings_with_same_first_and_last_char(color)
print("Number of strings with the same first and last character:", result)
