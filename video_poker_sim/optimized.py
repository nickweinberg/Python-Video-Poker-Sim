# lets try to optimize this
import numpy as np

import itertools
import random
import pprint

import sys
import os

from evaluators import isRoyalFlush, isStraightFlush, isOfAKind, isFullHouse, isFlush, isStraight, isTwoPair, isJacksOrBetter

print_color = { 1 : 'C', 2: 'S', 3: 'D', 4: 'H' }
print_num = {1:'A', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'J', 12:'Q', 13:'K'}



def make_deck():
    # initialize the 52 cards
    color = [1,2,3,4] #names of suits dont matter
    value = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    deck = []

    for c in color:
        for v in value:
            deck.append((v,c))

    random.shuffle(deck)
    return deck

def deal_hand(deck):
    hand = [deck.pop() for _ in range(5)]
    return hand, deck


deck = make_deck()
hand, deck = deal_hand(deck)


"""
To optimize let's solve the playing strategy first.

Create a lookup table where based on cards gives us best EV play

"""

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

# 16 is for the maximum number of paying hands on the draw


# loop through 2,598,960 combinations of 5 cards out of 52

# score according to poker value

# put the score in d_zero.
# first hand in element 0
# 2nd hand in element 1...


# for each of the 5 ways to choose 4 cards on the deal
# translate the four cards  into an index number from
# 0 to 270,724
# then increment element[index number][hand score] of d_one by 1


# for each of the 10 ways to choose 3 out of 5 cards on the deal, translate
# the three cards into an index number from 0 to 22,099
# then increment element[index number][hand score] of d_two by 1


# For each of the 10 ways to choose 2 out of 5 cards on the deal,
# translate the two cards into an  index number from 0 to 1,325,
# and increment element [index number][hand score] of array3 by 1.


# For each of the 5 ways to choose 1 out of 5 cards on the deal, translate the card into an index number from 0 to 51, and increment
# element [index number][hand score] of array4 by 1.

# Increment element [hand score] of array5 by 1.



# Next, loop through the 134,459 classes of hands explained above.


# To determine the value of holding all five cards, translate the five cards to an index number,
# and look up the poker value in d_zero.