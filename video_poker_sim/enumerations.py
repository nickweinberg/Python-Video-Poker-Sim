import numpy as np
import scipy.misc as sc

import itertools
import random
import pprint
import csv

import sys
import os

from evaluators import isRoyalFlush, isStraightFlush, isOfAKind, isFullHouse, isFlush, isStraight, isTwoPair, isJacksOrBetter, payout

import timeit

start_time = timeit.default_timer()


# discard zero cards
d_zero = np.zeros(2598960)
# discard one card
d_one = np.zeros([270725, 16])
# discard two cards
d_two = np.zeros([22100, 16])
# discard three cards
d_three = np.zeros([1326, 16])
# discard four cards
d_four = np.zeros([52, 16])
# discard five cards
d_five = np.zeros(16)


# make deck of 52 cards
color = [1,2,3,4] #names of suits dont matter
value = [1,2,3,4,5,6,7,8,9,10,11,12,13]
cards = []
for c in color:
    for v in value:
        cards.append((v,c))

for i, hand in enumerate(itertools.combinations(cards, 5)):
    d_zero[i] = payout(hand)

updated_time = timeit.default_timer() - start_time
print('discard 5 time: ', updated_time)

a = np.asarray(d_zero)
np.savetxt("5_card_combos.csv", a, delimiter=',')

print('file saved')
