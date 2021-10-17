from os import name, system
import random
def clear():
    """Clears the terminal"""
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')

def rand_pick(list_of_elements):
    return random.choice(list_of_elements)

def deal_cards(list_of_elements, the_list, num_cards):
    times = 0
    while times < num_cards:
        card = rand_pick(list_of_elements)
        the_list.append(card)
        times += 1
    return the_list

# deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# user_cards = []
# user_cards = deal_cards(deck, user_cards, 2)
# print(user_cards)