#task 1
# def my_func(x):
#     x = x*x
#     return x
# x = float(input("Input number to square: "))
# y = my_func(x)
# print(y)

#task 4
# def count_most_frequent(container):
#     highest=None
#     occurance=0
#     for element1 in container:
#         element_occ= 0
#         for element2 in container:
#             if element1 == element2:
#                 element_occ += 1
#         if element_occ > occurance:
#             highest = element1
#             occurance = element_occ
#
#     return highest, occurance
# cont =['a','b','a','c']
# print(count_most_frequent(cont))
#task 5
# def count_most_frequent(container):
#     highest=None
#     occurance=0
#     dictionary = dict()
#     for i in container:
#         element_occ= container.count(i)
#         if not (i in dictionary):
#             dictionary[i] = element_occ
#
#     for key, value in dictionary.items():
#         if value >occurance:
#             highest = key
#             occurance = value
#
#     return highest
#
# cont =['a','b','a','c']
# print(count_most_frequent(cont))

#task 2
def go_to_lobby(gold_coins: int) -> None:
    """ The start of the adventure """
    print_gold_amount(gold_coins)
    print("You are in the lobby of the dungeon. What do you do?")
    print("1. Examine the lobby.")
    print("2. Go to the throne hall.")
    print("3. Leave.")
    option = int(input("enter any option: "))
    if option == 1:
        examine_lobby(gold_coins)
    elif option == 2:
        go_to_throne_hall(gold_coins)
    elif option == 3:
        leave(gold_coins)
    else:
        print("invalid option")


def examine_lobby(gold_coins: int) -> None:
    print_gold_amount(gold_coins)
    rob_amount = 10
    print("A band of goblins rob " + str(rob_amount) + " gold from you.")
    gold_coins = gold_coins-rob_amount
    go_to_lobby(gold_coins)

def leave(gold_coins: int) -> None:
    print_gold_amount(gold_coins)
    if gold_coins< 0:
        go_to_kitchen(gold_coins)
    print("You leave the dungeon.")

def go_to_throne_hall(gold_coins: int) -> None:
    print_gold_amount(gold_coins)
    print("You are in the throne hall. What do you do?")
    print("1. Examine the throne hall.")
    print("2. Go back to the lobby.")
    option = int(input())
    if option == 1:
        examine_throne_hall(gold_coins)
    elif option == 2:
        go_to_lobby(gold_coins)
    else:
        print("invalid option")

def examine_throne_hall(gold_coins: int) -> None:
    print_gold_amount(gold_coins)
    rob_amount = 40
    print("You disturb the dungeon keeper who makes you pay " + str(rob_amount) + " gold.")
    gold_coins=gold_coins-rob_amount
    go_to_throne_hall(gold_coins)

def go_to_kitchen (gold_coins):
    print_gold_amount(gold_coins)
    print(("You are in the kitchen of the dungeon. what you do?"))
    print("1. wash dishes. earn fourty gold coin")
    print("2. leave")
    option= int(input("enter the option: "))
    if option == 1:
        wash_dishes(gold_coins)
    elif option == 2:
        go_to_lobby(gold_coins)
    else:
        print("invalid option")

def wash_dishes(gold_coins):
    gold_coins+=40
    go_to_kitchen(gold_coins)
def print_gold_amount(gold_coins: int) -> None:
    print("You have " + str(gold_coins) + " gold.")

go_to_lobby(50)
