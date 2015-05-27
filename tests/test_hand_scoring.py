
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
        RF_hand = [
        [10,1], [11,1],[12,1], [9,1], [8,1]]

        not_RF_hand = [
        [1,1], [11,1],[12,1], [9,1], [8,1]]

        not_flush_royal_hand = [
        [12,1],[11,2],[10,3],[9,1],[8,1]]

        self.assertEqual(get_hand_type(RF_hand), 9)
        self.assertNotEqual(get_hand_type(not_RF_hand), 9)
        self.assertNotEqual(get_hand_type(not_flush_royal_hand), 9)

    def test_straight_flush(self):
        SF_hand = [
        [10,1], [11,1],[7,1], [9,1], [8,1]]

        self.assertEqual(get_hand_type(SF_hand), 8)

    def test_flush(self):
        flush_hand = [
        [1,2],[4,2],[9,2],[10,2],[13,2]]
        self.assertEqual(get_hand_type(flush_hand), 5)

    def test_four_of_a_kind(self):
        FoaK_hand = [
        [3,2],[3,3],[3,4],[3,1],[13,2]
        ]
        self.assertEqual(get_hand_type(FoaK_hand), 7)

    def test_full_house(self):
        full_house_hand = [[]]

    def test_straight(self):
        straight_hand= [[]]

    def test_three_of_a_kind(self):
        ToaK_hand = [[]]

    def test_two_pair(self):
        two_pair_hand = [[]]

    def test_jacks_or_better(self):
        JoB_hand = [[]]

    def test_no_win(self):
        no_win_hand = [[]]
