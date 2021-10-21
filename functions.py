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
    """takes a list to choose from, a list to add to, and how many times. returns the new list"""
    times = 0
    while times < num_cards:
        card = rand_pick(list_of_elements)
        the_list.append(card)
        times += 1
    return the_list

def card_add(cards):
    """Takes a list of numbers, adds them up, returns the sum of the numbers"""
    the_sum = 0
    for card in cards:
        the_sum += int(card)
    return int(the_sum)

def cardAdd4Compy(cards, deck ):
    """Takes compy cards and deck, adds compy cards; if less than 20, gives compy another. returns list of compy cards. """
    sumCards = card_add(cards)
    # There could be a better algorythm here that weighs the chances, and decides based on that
    if sumCards < 20: 
        cards = deal_cards(deck, cards, 1)
    return cards

def determine_winner(user_score, compy_score):
    """Takes the user score and compy score and determines if the loser won or lost. Returns 'Y' or 'N' to say whether the user won or not"""
    win = ''
    if user_score > 21:
        win = 'N'
    elif user_score <= 21 and compy_score < user_score:
        win = 'Y'
    else: 
        win = 'N'
    if user_score == compy_score:
        win = 'D'
    return win
# deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# user_cards = []
# user_cards = deal_cards(deck, user_cards, 2)
# print(user_cards)