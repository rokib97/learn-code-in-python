#check the players score
def player_1_wins(player_1_score, player_2_score):
    return player_1_score > player_2_score

# check and compare the heights of the characters
def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = edward_height == mustang_height
    is_alphonse_edward_same = edward_height == alphonse_height
    is_winry_alphonse_same = alphonse_height == winry_height
    
    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same

# check if the player has enough health to continue
def can_withstand_blow(hero_armor, enemy_damage):
    return hero_armor >= enemy_damage

#check if the player has enough health to continue
def print_status(player_health):
    if(player_health == 0):
        print("Player is dead")
    print("Status Check Complete")

# check if the plyer has enough soldiers for the army
def check_swords_for_army(number_of_swords, number_of_soldiers):
    if(number_of_swords == number_of_soldiers):
        return f"correct amount"
    return f"not enough soldiers"
    
# check if the player is dead, injured, or healthy
def player_status(health):
    if(health <= 0):
        status = "Player is dead"
    elif(health <= 5):
         status = "Player is injured"
    else:
        status = "Player is healthy"
    return status


# check if the player is the highest scoring player
def check_high_score(current_player_name, high_scoring_player_name):
    if (current_player_name == high_scoring_player_name):
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"


#check if the player is the highest or lowest scoring player
def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if(player_name == high_scoring_player_name):
        return "You are the highest scoring player!"
    elif(player_name == low_scoring_player_name):
        return "You are the lowest scoring player!"
    else:
        return "You are not the highest or lowest scoring player!"
    

#check if the attack hits the target
def does_attack_hit(attack_roll, armor_class):
    return (attack_roll != 1 and attack_roll >= armor_class) or attack_roll == 20
        

#check if the custermer is eligible to buy alcohol
def should_serve_customer(customer_age, on_break, time):
    return customer_age >= 21 and not on_break and time >= 5 and time <= 10


# check if the mount rental time is over
def check_mount_rental(time_used, time_purchased):
    if(time_used > time_purchased):
        return "You need to pay extra"
    return "Thank you for renting from us!"


# check if the player has enough health to continue
def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False
    if(player_power > enemy_defense):
        advantage = True
    elif(player_power < enemy_defense):
        disadvantage = True
    else:
        evenly_matched = True
    return advantage, disadvantage, evenly_matched


def has_enough_energy(energy_available, distance_one_way, meters_per_energy):
    total_distance = distance_one_way * 2
    energy_nedded = total_distance / meters_per_energy
    
    return energy_available >= energy_nedded
