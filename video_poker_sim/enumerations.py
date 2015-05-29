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
    return '-'.join(sorted(combo))

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


# one_card_combos =
# two_card_combos =
# three_card_combos =
# four_card_combos =
# five_card_combos

# print(load_dicts('total_hand_combos_one.p'))

total_hand_type_combos = [0 for _ in range(9)]
# Loop through all 2,598,960 (or w/e possible hands)

# 1) Score the hand to determine what hand type it is.

# 2) Update total number of hands of type H
# total_hand_type_combos[H] += 1

# 3) For each of 5 individual cards, update the total
#    number of hands of type H which include that card
#    one_card_combos['CARD_STR'][H] += 1

# 4) For each of 10 combinations of 2 cards, update the total
#    number of hands of type H which include both cards
#    two_card_combos['C1-C2'][H] += 1

# 5) For each of the 10 combinations of 3 cards, update the total
#    number of hands of type H which includ all three cards
#    three_card_combos['C1-C2-C3'][H] += 1


# 6) For each of the 5 combinations of 4 cards, update the total
#    number of hands of type H which include all four cards.
#    four_card_combos['C1-C2-C3-C4'][H] += 1


# 7) Update five_card_combos
#    five_card_combos['C1-C2-C3-C4-C5'][H] = 1

# create_dicts_and_save()

