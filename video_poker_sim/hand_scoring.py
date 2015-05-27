import numpy as np

"""
hand_scoring.py

idea from :
https://web.archive.org/web/20120509212547/http://www.vpgenius.com/video-poker/jacks-or-better.aspx#


"""

def get_hand_type(hand):
    #
    c1,c2,c3,c4,c5 = hand
    r1,r2,r3,r4,r5 = c1[0],c2[0],c3[0],c4[0],c5[0] #ranks
    s1,s2,s3,s4,s5 = c1[0],c2[0],c3[0],c4[0],c5[0] #suits

    # If all suits are the same it's a flush
    is_flush = (s1 == s2 and s2==s3 and s3==s4 and s4==s5)

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


    # if is_flush:
    #     if r1 == 8:
            # logically must



# Hand(Rank1, Suit1, ... Rank5, Suit5)
hand = np.array([[5,0], [12,1],[1,2], [1,3], [12,4]], dtype='int16')

get_hand_type(hand)
