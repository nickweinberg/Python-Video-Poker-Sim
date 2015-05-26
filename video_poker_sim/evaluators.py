
# def payout(hand):
#     # maybe read payouts from file
#     if isRoyalFlush(hand):
#         return bet_val * ROYAL

#     elif isStraightFlush(hand):
#         return bet_val * ST_FLUSH

#     elif isOfAKind(hand,4):
#         return bet_val * FOUR_KIND

#     elif isFullHouse(hand):
#         return bet_val * FULL_HOUSE

#     elif isFlush(hand):
#         return bet_val * FLUSH

#     elif isStraight(hand):
#         return bet_val * STRAIGHT

#     elif isOfAKind(hand,3):
#         return bet_val * THREE_KIND

#     elif isTwoPair(hand):
#         return bet_val * TWO_PAIR

#     elif isJacksOrBetter(hand):
#         # will be different w/ deuces wild
#         return bet_val * JACK_BETTER

#     else:
#         return 0





def payout(hand):
    # maybe read payouts from file
    if isRoyalFlush(hand):
        return 9
    elif isStraightFlush(hand):
        return 8
    elif isOfAKind(hand,4):
        return 7
    elif isFullHouse(hand):
        return 6
    elif isFlush(hand):
        return 5
    elif isStraight(hand):
        return 4
    elif isOfAKind(hand,3):
        return 3
    elif isTwoPair(hand):
        return 2

    elif isJacksOrBetter(hand):
        return 1

    else:
        return 0


def isFlush(hand):
    if(hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]):
        return True
    else:
        return False

def isStraight(hand):
    nums = []

    for i in range(0,len(hand)):
        nums.append(hand[i][0])

    nums.sort()

    isStraight = False
    for i in range(0,len(hand)-1):
        if(nums[i] == nums[i+1]-1):
            isStraight = True
        else:
            isStraight = False
            break

    #special case of 10,J,Q,K,A
    if(nums[0] == 1 and nums[1] == 10 and nums[2] == 11 and nums[3] == 12 and nums[4] == 13):
        isStraight = True

    return isStraight


def isStraightFlush(hand):
    if(isFlush(hand) and isStraight(hand)):
        return True
    else:
        return False


def isRoyalFlush(hand):
    nums = []

    for i in range(0,len(hand)):
        nums.append(hand[i][0])

    nums.sort()
    if(isStraightFlush(hand) and nums[0] == 1 and nums[1] == 10 and nums[2] == 11 and nums[3] == 12 and nums[4] == 13):
        return True
    else:
        return False


def isOfAKind(hand,k):
    cnt = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(0,len(hand)):
        cnt[hand[i][0]-1] += 1

    if k in cnt:
        return True
    else:
        return False


def isFullHouse(hand):
    cnt = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(0,len(hand)):
        cnt[hand[i][0]-1] += 1

    if 3 in cnt and 2 in cnt:
        return True
    else:
        return False

def isJacksOrBetter(hand):
    cnt = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(0,len(hand)):
        cnt[hand[i][0]-1] += 1

    if cnt[0] == 2 or cnt[10] == 2 or cnt[11] == 2 or cnt[12] == 2: #jacks or better pair
        return True

    else:
        return False

def isTwoPair(hand):
    cnt = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(0,len(hand)):
        cnt[hand[i][0]-1] += 1

    noOfPairs = 0
    for num in cnt:
        if num == 2:
            noOfPairs += 1

    if noOfPairs == 2:
        return True

    else:
        return False


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