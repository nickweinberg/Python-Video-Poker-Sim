import numpy as np
import scipy.misc as sc
import csv

import itertools
import random
import pprint

import sys
import os

from evaluators import isRoyalFlush, isStraightFlush, isOfAKind, isFullHouse, isFlush, isStraight, isTwoPair, isJacksOrBetter, payout

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
Idea: for every


"""


"""
EV = sum( payout * (payout hits/total draws))

"""