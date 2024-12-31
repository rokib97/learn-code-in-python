def get_inventory():
    return ["Healing Potion", "Leather Scraps", "Iron Helmet", "Shortsword"]


#list in multiple lines
flower_types = [
    "daffodil",
    "rose",
    "chrysanthemum"
]
# print(flower_types[0])


def get_leather_scraps():
    inventory = [
        "Healing Potion",
        "Leather Scraps",
        "Iron Helmet",
        "Bread",
        "Shortsword",
    ]

    item_index = 1

    return inventory[item_index]

#len 
fruits = ["apple", "banana", "pear"]
# print(len(fruits))


def get_last_index(inventory):
    inventory[0] = "Mango"
    print(inventory)
    return inventory[len(inventory) - 1]

# print(get_last_index(fruits))

def generate_user_list(num_of_users):
    player_ids = []

    for i in range(0, num_of_users):
        player_ids.append(i)

    return player_ids

# print(generate_user_list(5))


def clear_inventory():
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth",
    ]

    print(f"inventory: {inventory}")

    for i in range(0, len(inventory)):
        item = inventory.pop(len(inventory) -1)
        print(f"Selling: {item}")
        print(f"inventory: {inventory}")


def test():
    clear_inventory()
    print("=====================================")


def main():
    test()

# main()



def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0
    
    for i in range(0, len(items)):
        if items[i] == "Potion":
            potion_count += 1
        elif items[i] == "Bread":
            bread_count += 1
        elif items[i] == "Shortsword":
            shortsword_count += 1

    return potion_count, bread_count, shortsword_count


# print(get_item_counts(['Potion',"Bread","Shortsword",'Potion',"Bread","Shortsword"]))



trees = ['oak', 'pine', 'maple']

for tree in trees:
    pass
    # print(tree)
    

def contains_leather_scraps(items):
    found = False
    for item in items:
        if item == "Leather Scraps":
            found = True

    return found

# print(contains_leather_scraps(["Healing Potion", "Leather Scraps", "Iron Helmet", "Shortsword"]))


def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]
    unique_indexes =[]
    for i in range(0, len(old_character_levels)):
        if old_character_levels[i] != new_character_levels[i]:
            unique_indexes.append(i)
        
    return unique_indexes  

result = check_character_levels()
for i in result:
    pass
    # print(i)
    
negative_infinity = float("-inf")
positive_infinity = float("inf")

# print(positive_infinity, negative_infinity)

def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num
            
    return max_so_far

# print(find_max([45,55,44,3,2]))


def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        if i % 2 != 0:
            odd_numbers.append(i)

    return odd_numbers

# print(get_odd_numbers(9))

#slicing

scores = [50, 70, 30, 20, 90, 10, 50]

def get_champion_slices(champions):
    value1 = champions[2:]
    value2 = champions[:-2]
    value3 = champions[::2]
    
    return value1, value2, value3
# print(get_champion_slices(['rahim', "karim", "sakib", "babu", "tani"]))


def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    return favorite_weapons + favorite_armor + favorite_items

# print(concatenate_favorites(["knife"],["shield"],["dragger"]))


def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]
    return weapon in top_weapons
            
# print(is_top_weapon("silver"))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[-2:]


def trim_strongholds(strongholds):
    del strongholds[0]
    del strongholds[-2:]
    

# Tuples
my_tuple = ("hello",45, True)
dog_name, dog_age, is_dog = my_tuple
# print(my_tuple[1])
dog = ('Fodo',)

my_tuples2 = [("this is the first tuple in the list", 45, True),("this is the second tuple in the list", 21, False)]

# print(my_tuples2[0][1])


def get_heroes():
    heroes = [
        ("Glorfindel",2093,True),
        ("Gandalf",1054,False),
        ("Gimli",389,False),
        ("Aragorn",87,False)
    ]

    return heroes


# print(type(get_heroes()))


def get_first_item(items):
    return items[0]


def reverse_array(items):
    new_arr = []
    for i in range(len(items) -1, -1, -1):
        new_arr.append(items[i])
    return new_arr

# print(reverse_array([1, 2, 3]))

message = "hello there sam"
splited = message.split()
# print("".join(splited))

def filter_messages(messages):
    filtered_msg = []
    count_of_words = []
    
    for msg in messages:
        words = msg.split()
        non_bad_words =[]
        counter = 0
        for word in words:
            if word == "dang":
                counter += 1
            else:
                non_bad_words.append(word)
            
        filtered_msg.append(" ".join(non_bad_words))
        count_of_words.append(counter)
    return filtered_msg, count_of_words


messages = ["dang it bobby!", "look at it go"]
# print(filter_messages(messages)) 


def get_odds_and_evens(numbers):
    num_odds = 0
    num_evens = 0
    
    for num in numbers:
        if num % 2 == 0:
            num_evens += 1
        else:
            num_odds += 1
    return [num_evens, num_odds]

# print(get_odds_and_evens([23,4,44,2,3,6,7]))

def split_players_into_teams(players):
    even_teams = players[0::2]
    even_teams = players[1::2]
    
    
def check_ingredient_match(recipe, ingredients):
    count_ingredient = 0
    missing_ingredients = []
    for item in recipe:
        if not item in ingredients:
            missing_ingredients.append(item)
        else:
            count_ingredient += 1
    percentage_of_ingredients = (count_ingredient / len(ingredients)) * 100
    
    return percentage_of_ingredients, missing_ingredients
recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
ingredients = ["Dragon Scale", "Goblin Ear", "Phoenix Feather", "Troll Tusk"]

# print(check_ingredient_match(recipe, ingredients))


def validate_path(expected_path, character_path):
    name = character_path[:1]
    count = 0
    for index in range(len(expected_path)):
        if expected_path[index] == character_path[index + 1]:
            count += 1
        
    return name, count / len(expected_path) * 100
        

expected_path = ["A", "B", "C", "D"]
character_path = ["Hero123", "A", "C", "B", "D"]
# print(validate_path(expected_path, character_path))


def double_string(string):
    doubled_string = []
    for char in string:
        doubled_string.append(char * 2)
        
    return "".join(doubled_string)

# print(double_string("Rokib"))


