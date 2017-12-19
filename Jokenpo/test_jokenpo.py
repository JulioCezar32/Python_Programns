import unittest
from jokenpo import Jokempo
import random

    
class TestJokempo(unittest.TestCase):

    def setUp(self):
        self.list = ['stone', 'scissor', 'paper']

        x = random.choice(self.list)
        y = random.choice(self.list)
        self.jog_1 = Jokempo(x, y)
        self.jog_2 = Jokempo('stone', 'stone')

    def test_1(self):
        self.assertEqual('Draw', self.jog_1.play())

    def test_2(self):
        self.assertEqual('Draw', self.jog_2.play())

    def test_3(self):
        self.assertEqual('Draw', self.jog_2.play())

if __name__ == '__main__':
    unittest.main()