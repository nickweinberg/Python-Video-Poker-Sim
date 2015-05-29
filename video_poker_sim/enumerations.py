import numpy as np
import itertools

import numpy as np
import scipy.misc as sc
import cPickle as pickle

import itertools
from itertools import combinations

import sys
import os

import timeit

from hand_scoring import get_hand_type, payout
"""
1) Enumerate all the possibilties.
2) Save these data structures to disc.
-That way we only have to run this operation once.

"""
def sort_and_join(combo):
    # str combo ie. ['12', '13']
    return '-'.join(sorted(combo))

def create_deck():
    # returns deck
    color = [1,2,3,4]
    value = [0,1,2,3,4,5,6,7,8,9,10,11,12]

    color_str = [str(c) for c in color]
    value_str = [str(v) for v in value]

    return [[v, c] for c in color for v in value]

def create_dicts_and_save():
    start_time = timeit.default_timer()
    # create deck
    color = [1,2,3,4] #names of suits dont matter
    value = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    color_str = [str(c) for c in color]
    value_str = [str(v) for v in value]

    deck = [''.join([v, c]) for c in color_str
                          for v in value_str ]

    """
    possible hand ranks = 0,1,2,3,4,5,6,7,8,9

    {
        # index is hand rank, value is # of possibilities
        'CARD_STR': [0,0,0,0,0,0,0,0,0]
    }
    """
    total_hand_combos = [0 for _ in range(9)]
    # total # of combinations of each hand type for individual card
    total_hand_combos_one = {card: [0 for _ in range(9)] for card in deck}

    # "  " for two cards
    total_hand_combos_two = {sort_and_join(combo): [0 for _ in range(9)]
                                for combo in combinations(deck, 2)}
    # "  " for three cards
    total_hand_combos_three = {sort_and_join(combo): [0 for _ in range(9)]
                                    for combo in combinations(deck, 3)}
    # "  " for four cards
    total_hand_combos_four = {sort_and_join(combo): [0 for _ in range(9)]
                                    for combo in combinations(deck, 4)}

    # " " for five cards - a dealt hand. each hand type is easy 0 or 1
    total_hand_combos_five = {sort_and_join(combo): [0 for _ in range(9)]
                                    for combo in combinations(deck, 5)}


    print('runtime: %f') % (timeit.default_timer() - start_time)

    # save to disk
    pickle.dump(total_hand_combos_one, open('data/total_hand_combos_one.p', 'wb'))
    pickle.dump(total_hand_combos_two, open('data/total_hand_combos_two.p', 'wb'))
    pickle.dump(total_hand_combos_three, open('data/total_hand_combos_three.p', 'wb'))
    pickle.dump(total_hand_combos_four, open('data/total_hand_combos_four.p', 'wb'))
    pickle.dump(total_hand_combos_five, open('data/total_hand_combos_five.p', 'wb'))

    print('files saved')


def load_dicts(filename):
    # one_c = pickle.load(open('data/total_hand_combos_one.p', 'rb'))
    # two_c = pickle.load(open('data/total_hand_combos_two.p', 'rb'))
    # three_c = pickle.load(open('data/total_hand_combos_three.p', 'rb'))
    # four_c = pickle.load(open('data/total_hand_combos_four.p', 'rb'))
    # five_c = pickle.load(open('data/total_hand_combos_five.p', 'rb'))
    return pickle.load(open('data/%s' % (filename), 'rb'))

def str_to_card(card_str):
    # intput: card_str. ex. '131' or '11', etc.
    # returns tuple (int, int)
    if len(card_str) == 3:
        rank = int(card_str[0:2])
        suit = int(card_str[2])
    elif len(card_str) == 2:
        rank = int(card_str[0])
        suit = int(card_str[1])
    return rank, suit

def str_to_card_str(card_str):
    str_list = []
    if len(card_str) == 3:
        str_list.append(card_str[0:2])
        str_list.append(card_str[2])
    elif len(card_str) == 2:
        str_list.append(card_str[0])
        str_list.append(card_str[1])
    return ''.join(str_list)


def cards_to_str(hand):
    return [''.join([str(c[0]), str(c[1])]) for c in hand]



# three_card_combos =
# four_card_combos =
# five_card_combos

# Loop through all 2,598,960 (or w/e possible hands)

def main():
    start_time = timeit.default_timer() # timer to track runtime length

    deck = create_deck() # create deck
    total_hand_type_combos = [0 for _ in range(9)]

    # load dictionaries
    one_card_combos   = load_dicts('total_hand_combos_one.p')
    two_card_combos   = load_dicts('total_hand_combos_two.p')
    three_card_combos = load_dicts('total_hand_combos_three.p')
    four_card_combos  = load_dicts('total_hand_combos_four.p')
    five_card_combos  = load_dicts('total_hand_combos_five.p')

    for hand in combinations(deck, 5):
        # hand :: ex. ([0, 1],[3,4],[4,4],[8,4],[12,4])

        # 1) Score the hand to determine what hand type it is.
        # hand score 9 -> 8. (index of arrays - 1)
        hand_score_index = get_hand_type(hand) - 1

        # 2) Update total number of hands of type H
        total_hand_type_combos[hand_score_index] += 1

        # 3) For each of 5 individual cards, update the total
        #    number of hands of type H which include that card
        for card in hand: # card :: [0, 1]
            one_card_combos[''.join(
                [str(card[0]), str(card[1])])][hand_score_index] += 1

        # 4) For each of 10 combinations of 2 cards, update the total
        #    number of hands of type H which include both cards
        #    two_card_combos['C1-C2'][H] += 1
        for combo in combinations(hand, 2):
            two_card_str = sort_and_join(cards_to_str(combo))
            two_card_combos[two_card_str][hand_score_index] += 1

        # 5) For each of the 10 combinations of 3 cards, update the total
        #    number of hands of type H which includ all three cards
        #    three_card_combos['C1-C2-C3'][H] += 1
        for combo in combinations(hand, 3):
            three_card_str = sort_and_join(cards_to_str(combo))
            three_card_combos[three_card_str][hand_score_index] += 1

        # 6) For each of the 5 combinations of 4 cards, update the total
        #    number of hands of type H which include all four cards.
        #    four_card_combos['C1-C2-C3-C4'][H] += 1
        for combo in combinations(hand, 4):
            four_card_str = sort_and_join(cards_to_str(combo))
            four_card_combos[four_card_str][hand_score_index] += 1

        # 7) Update five_card_combos
        #    five_card_combos['C1-C2-C3-C4-C5'][H] = 1
        five_card_str = sort_and_join(cards_to_str(hand))
        five_card_combos[five_card_str][hand_score_index] = 1

    # save to disk
    pickle.dump(one_card_combos, open('data/one_card_hand_type.p', 'wb'))
    pickle.dump(two_card_combos, open('data/two_card_hand_type.p', 'wb'))
    pickle.dump(three_card_combos, open('data/three_card_hand_type.p', 'wb'))
    pickle.dump(four_card_combos, open('data/four_card_hand_type.p', 'wb'))
    pickle.dump(five_card_combos, open('data/five_card_hand_type.p', 'wb'))

    print('files saved')
    print('runtime: %f') % (timeit.default_timer() - start_time)



# create_dicts_and_save()


print('starting')

main()

