import unittest
from jokenpov2 import Jokenpo
class TestJokenpo(unittest.TestCase):

    unittest.TestCase._tipos = tipos = ['pedra', 'papel', 'tesoura']

    def tests_empate(self):
        for tipo in self._tipos:
            self.assertEquals(Jokenpo.result(tipo,tipo),'empate')
    def tests_vitoria(self):
        self.assertEquals(Jokenpo.result('pedra','tesoura'),'vitoria')
        self.assertEquals(Jokenpo.result('pedra','papel'),'derrota')
        self.assertEquals(Jokenpo.result('tesoura','pedra'),'derrota')
        self.assertEquals(Jokenpo.result('tesoura','papel'),'vitoria')
        self.assertEquals(Jokenpo.result('papel','tesoura'),'derrota')
        self.assertEquals(Jokenpo.result('papel','pedra'),'vitoria')

    def test_tipo_valido(self):
        for tipo_jog_1 in self._tipos:
            for tipo_jog_2 in self._tipos:
                self.assertEquals(Jokenpo.tipo_valido(tipo_jog_1, tipo_jog_2),'valido')

    def test_tipo_invalido(self):
        self.assertEquals(Jokenpo.tipo_valido('pedra','camelo'),'invalido')

if __name__ == '__main__':
    unittest.main()
