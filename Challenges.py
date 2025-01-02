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
    pass
    # print(factorial_recursive(-1))
except ValueError as e :
    pass
    # print(e)
    
    
    
def area_sum(rectangles):
    sum = 0
    for item in rectangles:
        sum += item['height'] * item['width']
        
    
    return sum

    

area_sum([
    {
        "height": 3,
        "width": 9
    },
    {
        "height": 3,
        "width": 3
    }
])
    
    
    
def fizzbuzz(start, end):
    my_list =[]
    for i in range(start, end):
        if i % 5 == 0 and i % 3 == 0:
            my_list.append("fizzbuzz")
        elif i % 5 == 0:
            my_list.append("buzz")
        elif i % 3 == 0:
            my_list.append("fizz")
        else:
            my_list.append(i)
    return my_list

# print(fizzbuzz(1,8))


def divide_list(nums, divisor):
    new_list = []
    for num in nums:
        if num % divisor == 0:
            new_list.append(num / divisor)
    return new_list

divided_list = divide_list([6, 8, 10], 2)
# print(divided_list) 



def join_strings(strings):
    print(len(strings))
    new_string = ''
    for i in range(len(strings)):
        new_string += strings[i]
        
        if(i < len(string_list) -1):
            new_string += ','
        

    print(new_string)
string_list = ["hello", "my", "friend"]
joined_string = join_strings(string_list)
print(joined_string) # "hello,my,friend"