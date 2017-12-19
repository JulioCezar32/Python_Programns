import unittest
from jokenpo import Jokempo


class TestJokempo(unittest.TestCase):

    def setUp(self):
        self.jog_1 = 'stone'
        self.jog_2 = 'scissor'
        self.jog_3 = 'paper'

    def test_paper(self):
        self.assertEqual('Win', Jokempo.paper(self.jog_1))
        self.assertEqual('Lose', Jokempo.paper(self.jog_2))
        self.assertEqual('Draw',Jokempo.paper(self.jog_3))

    def test_stone(self):
        self.assertEqual('Win', Jokempo.stone(self.jog_2))
        self.assertEqual('Lose', Jokempo.stone(self.jog_3))
        self.assertEqual('Draw',Jokempo.stone(self.jog_1))

    def test_scissor(self):
        self.assertEqual('Win', Jokempo.scissor(self.jog_3))
        self.assertEqual('Lose', Jokempo.scissor(self.jog_1))
        self.assertEqual('Draw', Jokempo.scissor(self.jog_2))


if __name__ =='__main__':
    unittest.main()