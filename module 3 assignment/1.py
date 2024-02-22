#Write a Python function to get the largest number, smallest num and sumof all from a list
def get_largest_smallest_sum(numbers):
    if not numbers:
        return None, None, 0  
    largest = smallest = numbers[0]  
    total_sum = numbers[0] 
    for num in numbers[1:]:
        if num > largest:
            largest = num
        elif num > smallest:
            smallest = num
        total_sum += num
    
    return largest, smallest, total_sum


numbers_list = [1,3,5,7,9,11,13,15]
largest, smallest, total_sum = get_largest_smallest_sum(numbers_list)

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Sum of all numbers: {total_sum}")
