import numpy as np
import scipy.misc as sc
import csv

import itertools
from itertools import combinations
import random
import pprint

import sys
import os

from hand_scoring import get_hand_type, payout

import timeit
start_time = timeit.default_timer()

print_color = { 1 : 'C', 2: 'S', 3: 'D', 4: 'H' }
print_num = {1:'A', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'J', 12:'Q', 13:'K'}



def make_deck():
    # initialize the 52 cards
    color = [1,2,3,4] #names of suits dont matter
    value = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    deck = []
    for c in color:
        for v in value:
            deck.append([c,v])

    random.shuffle(deck)
    return deck

def deal_hand(deck):
    hand = [deck.pop() for _ in range(5)]
    return hand, deck

def draw_cards(deck, hand, n):
    # draw n cards
    for i in n:
        hand.append(deck[-i])
    return hand

deck = make_deck()
dealt_hand, deck = deal_hand(deck)
# current_best_hold =
current_best_EV = 0

# for every possible hold
hold_5 = dealt_hand
current_best_EV = payout(get_hand_type(hold_5))

hold_4_combos = combinations(dealt_hand,4)
for hand in hold_4_combos:


# hold_3_combos = combinations(hand, 3)
# hold_2_combos = combinations(hand, 2)
# hold_1_combos = combinations(hand, 1)
# hold_0 = draw_new_hand(deck)

# check EV,

# if higher than current EV, keep it


# print highest EV


print(timeit.default_timer() - start_time)