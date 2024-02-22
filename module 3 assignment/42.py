# Write a Python function to check whether a number is in a given range

def check_in_range(number, start, end):
    
    
    if start <= number <= end:
        print(num, "is in the range", range_start, "-", range_end)
    else:
        print(num, "is not in the range", range_start, "-", range_end)

num = 5
range_start = 1
range_end = 10
check_in_range(num, range_start, range_end)