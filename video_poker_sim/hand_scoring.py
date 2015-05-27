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


    pass


# Hand(Rank1, Suit1, ... Rank5, Suit5)
hand = np.array([[1,0], [1,1],[1,2], [1,3], [12,4]], dtype='int16')

get_hand_type(hand)
