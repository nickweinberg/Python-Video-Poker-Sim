import itertools
import random
import pprint

import sys
import os

from evaluators import isRoyalFlush, isStraightFlush, isOfAKind, isFullHouse, isFlush, isStraight, isTwoPair, isJacksOrBetter
# start of just want some functions that will probably be useful


#implements n! where 'n' is integar
def factorial(n):
    # do i really want to use recursion here?
    if n==1 or n==0:
        # base case
        return 1
    else:
        return n*factorial(n-1)

def combination(n, k):
    # nCk where n and k are integers
    num = factorial(n)
    denom = factorial(n-k) * factorial(k)
    return num / denom

def create_new_deck():
    deck = []
    for c in card:
        deck.append(c)




#initialize the current dealt hand and modify the deck
def init_hand():
    # global deck
    global deck
    global hand
    global all_possible_holds
    global user_holds
    global index

    del deck[:]
    del hand[:]
    del all_possible_holds[:]
    del user_holds[:]
    index = 0

    #current deck
    for c in card:
        deck.append(c)

    # shuffle
    random.shuffle(deck)

    # deal hand
    while (len(hand) < 5):
        hand.append(deck.pop())



def payout(hand):
    # maybe read payouts from file
    if isRoyalFlush(hand):
        return bet_val * ROYAL

    elif isStraightFlush(hand):
        return bet_val * ST_FLUSH

    elif isOfAKind(hand,4):
        return bet_val * FOUR_KIND

    elif isFullHouse(hand):
        return bet_val * FULL_HOUSE

    elif isFlush(hand):
        return bet_val * FLUSH

    elif isStraight(hand):
        return bet_val * STRAIGHT

    elif isOfAKind(hand,3):
        return bet_val * THREE_KIND

    elif isTwoPair(hand):
        return bet_val * TWO_PAIR

    elif isJacksOrBetter(hand):
        # will be different w/ deuces wild
        return bet_val * JACK_BETTER

    else:
        return 0


def evaluate():

    global all_possible_holds
    global index
    global match_flag
    global match_cnt
    global no_of_deals

    print "evaluating...."

    del all_possible_holds[:]
    index = 0

    # all 32 possible strategies (hold possibilities) for a dealt hand ( need to calculate expected value for each of these )
    for i in range(0,len(hand)+1):
        for subset in itertools.combinations(hand,i):
                all_possible_holds.append(subset)

    # build all possible trial hands by brute force and calculate expected value for all possible hold strategies
    #trial_hand = []
    expected_value = []
    for item in all_possible_holds:
        number_of_draws = 5-len(item)
        no_all_possible_draws = combination(len(deck),number_of_draws)
        payout_running_sum = 0.0
        sets = itertools.combinations(deck,number_of_draws)
        for subset in sets:
            #trial_hand.append(item + subset)
            trial_hand = item + subset
            payout_running_sum = payout_running_sum + payout(trial_hand)
        expected_value.append(payout_running_sum/no_all_possible_draws)


    #find hold strategy with maximum expected value
    max_val = 0.0
    for i in range(0,len(expected_value)):
        if expected_value[i] > max_val:
            max_val = expected_value[i]
            index = i

    print "hold: "
    for item in all_possible_holds[index]:
        print print_num[item[0]],
        print print_color[item[1]],
        print ' ',
    print ''

    print "with expected value: ",
    print max_val


#### CONTSTANTS ####

bet_val = 1.00 #1$

#payout table
ROYAL = 800
ST_FLUSH = 50
FOUR_KIND = 25
FULL_HOUSE = 9
FLUSH = 6
STRAIGHT = 4
THREE_KIND = 3
TWO_PAIR = 2
JACK_BETTER = 1

color = [1,2,3,4] #names of suits dont matter

# need to figure way to do wildcards
value = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# value = [1,'w',3,4,5,6,7,8,9,10,11,12,13]
card = [] #describes all 52 cards in a deck in the form of < list of a (number, color) tuple >

print_color = { 1 : 'C', 2: 'S', 3: 'D', 4: 'H' }
print_num = {1:'A', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'J', 12:'Q', 13:'K'}

# initialize the 52 cards
for c in color:
    for v in value:
        card.append((v,c))


deck = []       #current deck
hand = []       #dealt hand

all_possible_holds = []
user_holds = []
index = 0
match_flag = False

no_of_deals = 0
match_cnt = 0

init_hand()
print "dealt hand: "
for i in range(0, len(hand)):
    print print_num[hand[i][0]],
    print print_color[hand[i][1]],
    print ' ',
print ''


evaluate()
""" doing multiple hands will be easy. Instead of get result from each hand once, get it n times. """



