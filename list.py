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