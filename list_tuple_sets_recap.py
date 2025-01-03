course = ['Python', 'Java', 'C++', 'JavaScript']

# print(len(course))
# print(course[0])
# print(course[-1])

# print(course[0:2]) #['Python', 'Java']
# print(course[:2]) #['Python', 'Java']
# print(course[2:]) #['C++', 'JavaScript']

# course.append('C#') #['Python', 'Java', 'C++', 'JavaScript', 'C#']
# course.insert(0, 'Ruby') #['Ruby', 'Python', 'Java', 'C++', 'JavaScript', 'C#']
# course.extend(['Go', 'Rust']) #['Ruby', 'Python', 'Java', 'C++', 'JavaScript', 'C#', 'Go', 'Rust']
# course.remove('Java') #['Ruby', 'Python', 'C++', 'JavaScript', 'C#', 'Go', 'Rust']
# course.pop() #['Ruby', 'Python', 'C++', 'JavaScript', 'C#', 'Go']
# course.pop(1) #['Ruby', 'C++', 'JavaScript', 'C#', 'Go']
# print(course.index('C++')) #1

# course.reverse() #['JavaScript', 'C++', 'Java', 'Python']
# course.sort() #['C++', 'Java', 'JavaScript', 'Python']
# course.sort(reverse=True) #['Python', 'JavaScript', 'Java', 'C++']

# sorted_courses = sorted(course) #['C++', 'Java', 'JavaScript', 'Python']
# print(sorted_courses)


nums = [1, 5, 2, 4, 3]

# print(min(nums)) #1
# print(max(nums)) #5
# print(sum(nums)) #15


# print(nums.index(5)) #1
# print(5 in nums) #True


for item in course:
    pass
    # print(item)



for index , item in enumerate(course, start=1):
    pass
    # print(index, item)       
    
    
# course_str = ", ".join(course)
course_str = " - ".join(course)
# print(course_str)
new_list = course_str.split(" - ")
# print(new_list)



tuple_1 = ('Python', 'Java', 'C++', 'JavaScript')
# print(tuple_1[0]) #Python
# print(tuple_1[1:3]) #('Java', 'C++')
# print(tuple_1[-1]) #JavaScript
# print(tuple_1[1:]) #('Java', 'C++', 'JavaScript')
# print(tuple_1[:2]) #('Python', 'Java')
# print(tuple_1[0:2]) #('Python', 'Java')
# print(tuple_1 + ('C#', 'Go')) #('Python', 'Java', 'C++', 'JavaScript', 'C#', 'Go')
# print(len(tuple_1)) #4
# print(tuple_1.index('C++')) #2
# print('C++' in tuple_1) #True

for item in tuple_1: 
    pass 
    # print(item)


# tuple_1[0] = 'Ruby' #TypeError: 'tuple' object does not support item assignment
# tuple_1.append('Ruby') #AttributeError: 'tuple' object has no attribute 'append'
# tuple_1.insert(0, 'Ruby') #AttributeError: 'tuple' object has no attribute 'insert'
# tuple_1.remove('Java') #AttributeError: 'tuple' object has no attribute 'remove'
# tuple_1.pop() #AttributeError: 'tuple' object has no attribute 'pop'
# tuple_1.sort() #AttributeError: 'tuple' object has no attribute 'sort'
# tuple_1.reverse() #AttributeError: 'tuple' object has no attribute 'reverse'
# tuple_1.extend('Ruby') #AttributeError: 'tuple' object has no attribute 'extend'


set_1 = {'Python', 'Java', 'C++', 'JavaScript'}
set_2 = {'Python', 'Java', 'C++', 'JavaScript', 'C#', 'Go'}

# print(set_1) 
# print('Python' in set_1) #True
# print('Ruby' in set_1) #False
# print(len(set_1)) #4

# print(set_2.difference(set_1))  #{'C#', 'Go'}


set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# print(set_a.difference(set_b)) #{1, 2}
# print(set_a.intersection(set_b)) #{3, 4}
# print(set_a.union(set_b)) #{1, 2, 3, 4, 5, 6}


empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} #This isn't right. It's a dictionary
empty_set = set() #This is correct

