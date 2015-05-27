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

def get_hand_type(hand):
    #
    c1,c2,c3,c4,c5 = hand
    r1,r2,r3,r4,r5 = c1[0],c2[0],c3[0],c4[0],c5[0] #ranks
    s1,s2,s3,s4,s5 = c1[1],c2[1],c3[1],c4[1],c5[1] #suits

    print(s1,s2,s3,s4,s5)
    # If all suits are the same it's a flush
    is_flush = (s1 == s2 and s2==s3 and s3==s4 and s4==s5)

    score = 0 #
    # sorts cards
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


    print(r1,r2,r3,r4,r5)
    print(is_flush)
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
             (r4 == r5-1)) or (r1==0 and r5==12):

            score = 8 # royal flush
            print('straight')


    return score



# Hand(Rank1, Suit1, ... Rank5, Suit5)
hand = np.array([
    [5,1], [12,1],[1,1], [1,1], [12,1]
], dtype='int16')

# get_hand_type(hand)

