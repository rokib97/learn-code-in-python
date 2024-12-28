# area_of_circle function
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

sword_length = 1.0
spear_length = 2.0

sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")




# multiple parameters
def triple_attack(damage_one, damage_two, damage_three):
    return damage_one + damage_two + damage_three

attack_one = 2
attack_two = 4
attack_three = 3
first_triple_attack_damage = triple_attack(attack_one, attack_two, attack_three)

print("Getting damage for", attack_one, attack_two, "and", attack_three, "...")
print(first_triple_attack_damage, "points of damage dealt!")
print("=====================================")

attack_four = -1
attack_five = 10
attack_six = 5
second_triple_attack_damage = triple_attack(attack_four, attack_five, attack_six)

print("Getting damage for", attack_four, attack_five, "and", attack_six, "...")
print(second_triple_attack_damage, "points of damage dealt!")
print("=====================================")


# Order of functions
def main():
    health = 10 
    armor = 5
    add_armor(health, armor)
    
def add_armor(h,a):
    new_health = h + a
    print_health(new_health)
    
def print_health(new_health):
    print(f"The player now has {new_health} health")
    
    
main()


# Hours_to_second 
def hours_to_second(hours):
    return hours * 60 * 60
    
result = hours_to_second(2)
print(result)
    

# Multiple return values
def cast_iceblast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana # return two values

dmg, mana = cast_iceblast(5, 100)
print(f"Damage: {dmg}, Remaining Mana: {mana}")



def become_warrior(first_name, last_name, power):
    title = f"{first_name} {last_name} the warrior"
    power += 1
    return title, power

result1, result2 = become_warrior("Frodo", "Baggins", 5)
print(result1, "has a power level of:", result2)


# Default values
def add_two_num(a,b=10):
    return a + b 

result = add_two_num(10,100)
print(result)



