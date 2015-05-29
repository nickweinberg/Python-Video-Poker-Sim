import numpy as np
import itertools

import numpy as np
import scipy.misc as sc
import csv

import itertools
from itertools import combinations
import random
import pprint

import sys
import os

import timeit

from hand_scoring import get_hand_type, payout
"""
1) Enumerate all the possibilties.
2) Save these data structures to disc.
-That way we only have to run this operation once.

"""
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
total_hand_combos_two = {','.join(combo): [0 for _ in range(9)]
                            for combo in combinations(deck, 2)}
# "  " for three cards
total_hand_combos_three = {','.join(combo): [0 for _ in range(9)]
                                for combo in combinations(deck, 3)}
# "  " for four cards
total_hand_combos_four = {','.join(combo): [0 for _ in range(9)]
                                for combo in combinations(deck, 4)}

# " " for five cards - a dealt hand. each hand type is easy 0 or 1
total_hand_combos_five = {','.join(combo): [0 for _ in range(9)]
                                for combo in combinations(deck, 5)}


print('runtime: %f') % (timeit.default_timer() - start_time)

# a = np.asarray(d_zero)
# np.savetxt("5_card_combos.csv", a, delimiter=',')

# print('file saved')
