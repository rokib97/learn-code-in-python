def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level":level,
        "rank": rank,
        "id": f"{name}#{server}" 
    }
    
    
# print(get_character_record("bloodwarrior123","server1", 3,3))


car = {
    "make": "tesla",
    "model": "3"
}
# print(car['model'])


planet = {}
planet["Earth"] = True
planet["Pluto"] = False

# print(planet["Earth"])


names = ["jack bronson", "jill mcarty", "john denver"]

names_dict = {}
for name in names:
    name_list = name.split()
    names_dict[name_list[0]] = name_list[1]
    

# print(names_dict)

full_names = ["jack bronson", "james mcarty", "jack denver"]
names_dict = {}
for full_name in full_names:
    names = full_name.split()
    first_name = names[0]
    last_name = names[1]
    names_dict[first_name] = last_name

del names_dict['jack']
# print(names_dict)


cars = {
    "ford": "f150",
    "tesla": "3"
}

# print("ford" in cars)

def count_enemies(enemy_names):
    enemies_dict = {}
    count = 1
    for enemy_name in enemy_names:
        if(enemy_name in enemies_dict):
            enemies_dict[enemy_name] = count + 1
        else:
            enemies_dict[enemy_name] = count 
    return enemies_dict
# print(count_enemies(['rokib','hasan','saki','rokib', 'saki']))


fruit_sizes = {
    "apple": "small",
    "banana": "large",
    "grape": "tiny"
}

for value in fruit_sizes:
    pass
    # print(fruit_sizes[value])


def get_most_common_enemy(enemies_dict):
    max_count = float("-inf")
    max_count_name = None
    for enemy in enemies_dict:
        if enemies_dict[enemy] > max_count:
            max_count = enemies_dict[enemy]
            max_count_name = enemy
    
    return max_count_name



my_dict = {
    "jackal": 1,
    "kobold": 2,
    "soldier": 3,
    "gremlin": 5  
}

# print(get_most_common_enemy(my_dict))



def get_quest_status(progress):
    return progress["entity"]['character']['quests']['Dragon_Slayer']['status']

result = get_quest_status({
    "entity": {
        "character": {
            "name": "Kaladin",
            "quests": {
                "Dragon_Slayer": {
                    "status": "In Progress",
                },
                "talk_to_syl": {
                    "status": "Completed",
                },
            },
        }
    }
})

# print(result)


def merge(dict1, dict2):
    merged_dict = {}
    for key in dict1:
        merged_dict[key] = dict1[key]
    for key in dict2:
        merged_dict[key] = dict2[key]   
two_towers = {"Frodo": "One Ring", "Aragorn": "Narsil"}
rotk = {"Aragorn": "Andúril", "Gandalf": "Glamdring"}
merged_dict = merge(two_towers, rotk)