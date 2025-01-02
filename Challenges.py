def number_sum(n):
    sum = 0
    for num in range(1,n+1):
       sum += num
    return sum
# print(number_sum(3)) #6

def find_min(nums):
    min_num = float('inf')
    for num in nums:
        if num < min_num:
            min_num = num

    return min_num
# print(find_min([1, 3, -1, 2]))


def remove_nonints(nums):
    new_list = []
    for num in nums:
        if type(num) == int:
            new_list.append(num)
    return new_list
# print(remove_nonints(['1', 1, '3', '400', 4, 500]))


def factorial(num):
    fact_result =  1
    if num == 0 or num == 1:
        return num 
    else:
        for i in range(num, 1, -1):
            fact_result *= i
    return fact_result
    



def factorial_recursive(num):
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursive(num - 1)
    
try:
    print(factorial_recursive(-1))
except ValueError as e :
    print(e)