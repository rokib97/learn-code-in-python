# Description: This file contains examples of how to use numbers in Python
#Calculating Damage
def calculate_damage(sword, arrow,spear,dagger, fireball):
    total_damage = sword + arrow + spear + dagger + fireball
    average_damage = total_damage / 5
    return total_damage, average_damage

total_damage, average_damage = calculate_damage(10, 15, 20, 25, 30)
# print(f"Total damage: {total_damage}, Average damage: {average_damage}")

# Normal Division vs Floor Division
# Normal Division Return a float
# Floor Division Return an integer
print(4/2) 
print(5//2)

# Exponents
# read as 2 to the power of 3

print(2 ** 3) # 2 * 2 * 2 = 8
print(2 ** 4) # 2 * 2 * 2 * 2 = 16
print(2 ** 5) # 2 * 2 * 2 * 2 * 2 = 32    


# Changing In Place
def update_player_score(current_score, increment):
    current_score = current_score + increment
    # current_score += increment # This is the same as the line above
    return current_score


# Plus Equals
star_rating = 4
star_rating += 1

# Minus Equals
health = 100
health -= 10

# Multiply Equals
damage = 20
damage *= 2

# Divide Equals
mana = 100
mana /= 2

# Modulus Equals
# Modulus is the remainder of a division operation
# 5 % 2 = 1
# 5 / 2 = 2 remainder 1
# 5 % 3 = 2
# 5 / 3 = 1 remainder 2
# 5 % 5 = 0
# 5 / 5 = 1 remainder 0


def get_hurt(current_health,damage):
    current_health -= damage
    return current_health

# print(get_hurt(100, 10))


# Calculate DPS
def calculate_dps(damage, time):
    dps = damage / time
    return dps

print(calculate_dps(8_000_000, 45))
print(calculate_dps(10_000_000, 49))


def binary_string_to_int(num_servers, num_players,num_admins):
    data_a = int(num_servers, 2)
    data_b = int(num_players, 2)
    data_c = int(num_admins, 2)
    return data_a, data_b, data_c
    
data_a, data_b, data_c = binary_string_to_int("101", "110", "111")
print(data_a, data_b, data_c)
