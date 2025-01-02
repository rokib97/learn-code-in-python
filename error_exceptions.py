# try:
#   10 / 0
# except Exception as e :
# #   print(e)
  
  
#   def main():
#     print(get_player_record(1))
#     print(get_player_record(2))
#     print(get_player_record(3))
#     print(get_player_record(4))


# # Don't edit below this line


# def main():
#     try:
#         print(get_player_record(1))
#         print(get_player_record(2))
#         print(get_player_record(3))
#         print(get_player_record(4))
#     except Exception as e:
#         pass
#         # print(e)
    
    
# def get_player_record(player_id):
#     if player_id == 1:
#         return {"name": "Slayer", "level": 128}
#     if player_id == 2:
#         return {"name": "Dorgoth", "level": 300}
#     if player_id == 3:
#         return {"name": "Saruman", "level": 4000}
#     raise Exception("player id not found")


# # main()



# def get_player_record(player_id):
#     if player_id == 1:
#         return {"name": "Slayer", "level": 128}
#     if player_id == 2:
#         return {"name": "Dorgoth", "level": 300}
#     if player_id == 3:
#         return {"name": "Saruman", "level": 4000}
#     raise Exception('player id not found')


# try:
#     print(get_player_record(3))
# except Exception as e:
#     pass
#     # print(e)
    
    
    
def handle_get_player_record(player_id):
    try:
        return get_player_record2(player_id)
    except IndexError:
        return 'index is too high'
    except Exception as e:
        return e
    
    
def get_player_record2(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]

# print(handle_get_player_record(-3))


def purchase_item(price, gold_available):
    if gold_available < price:
        raise Exception('not enough gold')
    return gold_available - price 

try:
    pass
    # print(purchase_item(50, 100))  
    # print(purchase_item(150, 100))  
except Exception as e:
    pass
    # print(e)  
    
    
def process_transactions(purchase_orders):
    leftovers = []
    for order in purchase_orders:
        try:
            remaining = purchase_item(order['price'], order['gold_available'])
            leftovers.append(remaining)
        except Exception as e:
            print(e)      
    return leftovers
def main():
    print("Processing transactions...")
    leftovers = process_transactions(
        [
            {"price": 10.00, "gold_available": 125.00},
            {"price": 5.00, "gold_available": 2.00},
            {"price": 20.01, "gold_available": 5.20},
            {"price": 1.04, "gold_available": 254.00},
            {"price": 40.20, "gold_available": 6.00},
            {"price": 16.00, "gold_available": 235.01},
            {"price": 10.70, "gold_available": 10.70},
            {"price": 12.00, "gold_available": 2.30},
        ]
    )
    print("Transactions complete!")
    print("Leftover amounts for successful purchases:")
    for leftover in leftovers:
        print(f" * {leftover:.2f}")


def purchase_item(price, gold_available):
    if gold_available < price:
        raise Exception(f"{gold_available:.2f} is not enough for {price:.2f}")
    return gold_available - price


main()