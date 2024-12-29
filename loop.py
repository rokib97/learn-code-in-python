def print_numbers():
    for i in range(0, 200):
        print(i)

# print_numbers()


def print_numbers_from_five_to():
    for i in range(5, 200):
        print(i)
        
# print_numbers_from_five_to()


def count_down():
    for i in range(100, 0, -5):
        print(i)
        
# count_down()

def count_down2():
    for i in range(5, 101, 5):
        print(i)
        
# count_down2()


def count_down_again(start, end):
    for i in range(start, end):
        print(i)
        
# count_down_again(1, 11)


def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total

sum = sum_of_numbers(1,6)
# print(sum)


def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total

sum_of_odd = sum_of_odd_numbers(6)
# print(sum_of_odd)



num = 0
while (num < 3):
    # print(num)
    num += 1
    

    
def regenerate(current_health, max_health, enemy_distance):
    while(current_health < max_health and enemy_distance > 3):
        current_health += 1
        enemy_distance -= 2
        
    return current_health

def countdown_to_start():
    for i in range(1,11):
        print(f"{i}...Fight")
        
# countdown_to_start()

def calculate_flurry_crit(num_attacks, base_damage):
    total_damage = 0
    for attack in range(num_attacks):
        if attack == num_attacks - 1:
            total_damage += base_damage * 4
        else:
            total_damage += base_damage * 2
    return total_damage
total_damage = calculate_flurry_crit(5, 10)
# print(total_damage)


