import numpy as np

"""
hand_scoring.py

idea from :
https://web.archive.org/web/20120509212547/http://www.vpgenius.com/video-poker/jacks-or-better.aspx#

Card Mappings:
0: 2
1: 3
2: 4
3: 5
4: 6
5: 7
6: 8
7: 9
8: Ten
9: Jack
10: Queen
11: King
12: Ace
"""

#### CONSTANTS ####
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

def payout(score):
    # maybe read payouts from file
    if score==9:
        return bet_val * ROYAL
    elif score==8:
        return bet_val * ST_FLUSH

    elif score==7:
        return bet_val * FOUR_KIND

    elif score==6:
        return bet_val * FULL_HOUSE

    elif score==5:
        return bet_val * FLUSH

    elif score==4:
        return bet_val * STRAIGHT

    elif score==3:
        return bet_val * THREE_KIND

    elif score==2:
        return bet_val * TWO_PAIR

    elif score==1:
        return bet_val * JACK_BETTER
    else:
        return 0

def get_hand_type(hand):
    # print(hand)
    c1,c2,c3,c4,c5 = hand
    r1,r2,r3,r4,r5 = c1[0],c2[0],c3[0],c4[0],c5[0] #ranks
    s1,s2,s3,s4,s5 = c1[1],c2[1],c3[1],c4[1],c5[1] #suits

    # If all suits are the same it's a flush
    is_flush = (s1 == s2 and s2==s3 and s3==s4 and s4==s5)

    score = 0 #
    # sort hand w/ bitwise XOR
    # TODO: test if this is faster than built-in sort
    if (r1 > r2):
        r1 = r1 ^ r2
        r2 = r2 ^ r1
        r1 = r1 ^ r2
    if (r1 > r3):
        r1 = r1 ^ r3
        r3 = r3 ^ r1
        r1 = r1 ^ r3
    if (r1 > r4):
        r1 = r1 ^ r4
        r4 = r4 ^ r1
        r1 = r1 ^ r4
    if (r1 > r5):
        r1 = r1 ^ r5
        r5 = r5 ^ r1
        r1 = r1 ^ r5
    if (r2 > r3):
        r2 = r2 ^ r3
        r3 = r3 ^ r2
        r2 = r2 ^ r3
    if (r2 > r4):
        r2 = r2 ^ r4
        r4 = r4 ^ r2
        r2 = r2 ^ r4
    if (r2 > r5):
        r2 = r2 ^ r5
        r5 = r5 ^ r2
        r2 = r2 ^ r5
    if (r3 > r4):
        r3 = r3 ^ r4
        r4 = r4 ^ r3
        r3 = r3 ^ r4
    if (r3 > r5):
        r3 = r3 ^ r5
        r5 = r5 ^ r3
        r3 = r3 ^ r5
    if (r4 > r5):
        r4 = r4 ^ r5
        r5 = r5 ^ r4
        r4 = r4 ^ r5

    # end sort

    if is_flush:
        if r1 == 8:
            # logically if hand is sorted
            # and it's a flush. Then  if first card is
            # a ten must be a royal flush.
            # We use similiar logic for other steps.
            score = 9 # Royal Flush
        elif ((r1 == r2-1) and
             (r2 == r3-1) and
             (r3 == r4-1) and
             ((r4 == r5-1) or (r1==0 and r5==12))):

            score = 8 # straight flush
        else:
            score = 5 # Flush

    else:
        # not flush cases
        if ((r1 == r3) and (r3 == r4) and ((r1 == r2) or (r4 == r5))):
            score = 7 # four of a kind

        elif ((r1 == r2) and (r4 == r5) and ((r2 ==r3) or (r3 ==r4))):
            score = 6 # full house

        elif ((r1 == r2-1) and
              (r2 == r3-1) and
              (r3 == r4-1) and
              ((r4 == r5-1) or (r1==0 and r5==12))):
            # same as straight flush just not a flush
            score = 4 # straight

        elif (((r1==r2) and (r2==r3)) or
              ((r2==r3) and (r3==r4)) or
              ((r3==r4) and (r4==r5))):
            score = 3 # Three of a Kind

        elif (((r1==r2) and (r3==r4)) or
              ((r1==r2) and (r4==r5)) or
              ((r2==r3) and (r4==r5))):
            score = 2 # Two Pair

        elif (((r1==r2) and (r1 >=9)) or
              ((r2==r3) and (r2 >=9)) or
              ((r3==r4) and (r3 >=9)) or
              ((r4==r5) and (r4 >=9))):
            score = 1 # jacks or better
        else:
            score = 0
    return score




