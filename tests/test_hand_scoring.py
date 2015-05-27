
import numpy as np
from nose2.tools import *
from video_poker_sim.hand_scoring import get_hand_type
import unittest


class HandScoringTestCase(unittest.TestCase):
    def setup(self):
        print "setup!"

    def teardown(self):
        print "tear down"

    def test_royal_flush(self):
        hand_to_test = np.array([
        [10,1], [11,1],[12,1], [9,1], [8,1]])
        hand_score = get_hand_type(hand_to_test)

        self.assertEqual(hand_score, 12)
