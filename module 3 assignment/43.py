# Write a Python function to check whether a number is perfect or not


def is_perfect_number(number):
    if number <= 0:
        return False

    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisors_sum == number

num = 28
is_perfect = is_perfect_number(num)

print(f"{num} is {'a' if is_perfect else 'not a'} perfect number.")