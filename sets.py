fruits = {"apple", "banana", "grape"}
fruits.add("pear")
# print(fruits)
# print(type(fruits))


names = set()
names.add("rokib")
# print(names)

for fruit in fruits:
    pass
    # print(fruit)
    
    
def remove_duplicates(spells):
    seen = set()
    unique_spells = []
    for spell in spells:
        if spell not in seen:
            seen.add(spell)
            unique_spells.append(spell)
            
    return unique_spells

spells = ["Fireball", "Frostbolt", "Fireball", "Arcane Blast", "Frostbolt"]
remove_duplicates(spells)

# Built in way 
def remove_duplicates2(spells):
    return list(set(spells))


def remove_duplicates2(lst):
    return set(spells)



def count_vowels(text):
    pass


def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for txt in text:
        if txt in vowels:
            count += 1

    return count
# print(count_vowels("rokibul hasan"))



def find_missing_ids(first_ids, second_ids):
    new_list = []
    print(list(set(first_ids) - set(second_ids)))
    


first_ids = [1,4,5,7]
second_ids = [5,7,8,9,10]
find_missing_ids(first_ids,second_ids)

