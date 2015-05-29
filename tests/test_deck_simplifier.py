import numpy as np
from nose2.tools import *
from video_poker_sim.deck_simplifier import get_suit_pattern
import unittest


class SuitPatternsTestCase(unittest.TestCase):
    def setup(self):
        print "setup!"

    def teardown(self):
        print "tear down"

    def test_basic_suit_pattern(self):
        test_flush_hand = [
            [10,1], [11,1],[12,1], [9,1], [8,1]]

        get_suit_pattern(test_flush_hand)

        test_no_flush_hand = [
            [10,1], [11,2],[12,3], [9,4], [8,1]]

        get_suit_pattern(test_no_flush_hand)