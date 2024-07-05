def add_two_nums(num1, num2):
    total = num1 + num2
    return total

# print(add_two_nums(10, 20))

def area_or_circle(r):
    pi = 3.14
    area = pi * r ** 2
    return area

# print(area_or_circle(5))

def add_all_nums(*nums):
    if all(isinstance(num, (int, float)) for num in nums):
        total = 0
        for num in nums:
            total += num
        return total
    else:
        return "Please enter number only"

# print(add_all_nums(2, 3, 5))

def convert_celsius_to_fahrenheit(c):
    temp = (c * 9 / 5) + 32
    return temp

# print(convert_celsius_to_fahrenheit(20))

def print_list(nums):
    for num in nums:
        print(num)

# print_list([2, 3, 4, 5])


