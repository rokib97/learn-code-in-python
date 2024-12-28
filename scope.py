# Scope

def subtract(x, y):
    return x - y
result = subtract(5, 3)
# print(x)
# ERROR! "name 'x' is not defined"



def get_max_health(modifier, level):
    return modifier * level

my_modifier = 5
my_level = 10

max_health = get_max_health(my_modifier, my_level)
print(f"max_health is: {max_health}")


# Global Scope
pi = 3.14

def get_area_of_circle(radius):
    return pi * radius * radius #pi can accessable here



player_level = 4

def calculate_health(modifier):
    return player_level * modifier

def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level

print(f"Character has {calculate_health(10)} max health.")

print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")