# Scope

def subtract(x, y):
    return x - y
result = subtract(5, 3)
# print(x)
# ERROR! "name 'x' is not defined"


# =============================================================== #

def get_max_health(modifier, level):
    return modifier * level

my_modifier = 5
my_level = 10

max_health = get_max_health(my_modifier, my_level)
print(f"max_health is: {max_health}")


# =============================================================== #


# Global Scope
pi = 3.14

def get_area_of_circle(radius):
    return pi * radius * radius #pi can accessable here

# =============================================================== #

player_level = 4

def calculate_health(modifier):
    return player_level * modifier

def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level

print(f"Character has {calculate_health(10)} max health.")

print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")





# =============================================================== #


# =============================================================== #

# Python uses the LEGB Rule to resolve variable names:
# L: Local
def my_function():
    local_variable = 10  # Local scope
    print(local_variable)

my_function()
# print(local_variable)  # This will raise a NameError

# To modify an enclosing variable from an inner function, use the nonlocal keyword:

def outer_function():
    enclosing_variable = "Hello"

    def inner_function():
        nonlocal enclosing_variable
        enclosing_variable = "Hi"

    inner_function()
    print(enclosing_variable)

outer_function()
# Output: Hi
# =============================================================== #




# =============================================================== #
# E: Enclosing
def outer_function():
    enclosing_variable = "Hello"

    def inner_function():
        print(enclosing_variable)  # Accessing the enclosing scope variable

    inner_function()

outer_function()
# =============================================================== #

# =============================================================== #

# G: Global
global_variable = 100 

def my_function():
    print(global_variable)  # Access global variable

my_function()

# To modify a global variable:

global_variable = 100

def modify_global():
    global global_variable
    global_variable = 200

modify_global()
print(global_variable)  # Output: 200



# =============================================================== #

# B: Built-in
# =============================================================== #
print(len([1, 2, 3]))  # len is a built-in function


# Variable shadowing 
x = 5  # Global

def shadow_example():
    x = 10  # Local scope
    print(x)  # Output: 10

shadow_example()
print(x)  # Output: 5
