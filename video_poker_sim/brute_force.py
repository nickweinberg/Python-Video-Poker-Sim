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
            deck.append([v,c])

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
hold_3_combos = combinations(dealt_hand, 3)
hold_2_combos = combinations(dealt_hand, 2)
hold_1_combos = combinations(dealt_hand, 1)

all_possible_holds = list(hold_4_combos) + list(hold_3_combos) + list(hold_2_combos) + list(hold_1_combos)


# print(list(combinations(dealt_hand,4)))

payout_running_sum = 0
expected_value = []

for hold in all_possible_holds:
    number_of_draws = 5-len(hold)
    no_all_possible_draws = sc.comb(len(deck), number_of_draws)
    payout_running_sum = 0.0
    sets = combinations(deck,number_of_draws)

    for drawn_cards in sets:
        payout_running_sum += payout(get_hand_type(hold + drawn_cards))

    expected_value.append(payout_running_sum/no_all_possible_draws)

max_val = 0.0
for i in range(0, len(expected_value)):
    if expected_value[i] > max_val:
        max_val = expected_value[i]
        index = i

print "hand: " + str(dealt_hand)
print "hold: " + str(all_possible_holds[index])
print "EV: " + str(max_val)
# hold_0 = draw_new_hand(deck)

# check EV,

# if higher than current EV, keep it


# print highest EV


print('runtime: %f') % (timeit.default_timer() - start_time)