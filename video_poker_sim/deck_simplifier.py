import numpy as np
import scipy.misc as sc
import csv

import itertools
import random
import pprint

import sys
import os


import timeit

"""
An attempt to simplify the deck by in some cases ignoring suits.
(idea from https://web.archive.org/web/20130213053427/http://www.vpgenius.com/articles/deck-simplification.aspx)

https://web.archive.org/web/20120509212547/http://www.vpgenius.com/video-poker/jacks-or-better.aspx#
Identify possible combinations for following core hands:

* Four of a Kind
* Full House
* Three of a Kind
* Two Pair
* One Pair
* No Pair

 4oaK has 2 ranks- 1for quads 1 for kicker
 3oak has 3 one for trips 1 for each kicker

 Full House is similar - one rank for the Three of a Kind and one rank for the Pair.
 Two Pair hands have three ranks,
 one for each Pair and one for the Kicker.

 One Pair hands have four ranks,
 the Pair and three Kickers.

 No Pair hands have five ranks,
 each of which must be different
 (otherwise it would be a different core hand type).

"""



"""
EV = sum( payout * (payout hits/total draws))

"""
start_time = timeit.default_timer()



# print(sc.comb(13,1) * sc.comb(12, 3))
def get_suit_pattern(hand):
    """
    Takes a hand and returns suit pattern in form:
    ex. 'ABCDA' - each letter represents different suit
    ex. 'AAAAA' - all cards are same suit
    ex. 'AAAAB' - one off a all same suit.
    """

    # turn hand into list of suits
    suits = [c[1] for c in hand]

    ss = set(suits) # suit sets

    print(suits)
    print(ss)
    #

    # if set is length 1 all are same

    # if set is length 2

    # if set is length 4 all different sans 1

# test_hand = [[1,2], [1]

# get_suit_pattern('test')


print('runtime: %f') % (timeit.default_timer() - start_time)