import unittest

class TestJokempo(unittest.TestCase):

    def test_empate(self):
        self.assertEquals(Jokempo.result('pedra','pedra'),'empate')
