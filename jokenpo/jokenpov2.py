#creating a jokenpo class
class Jokenpo:

    def __init__(self, jog_1, jog_2):
        self._jog_1 = jog_1
        self._jog_2 = jog_2

    def tipo_valido(self, jog_1,jog_2):

        tipos = ['pedra','papel','tesoura']

        if (jog_1 in tipos) and (jog_2 in tipos):
            return 'valido'
        else:
            return 'invalido'

    def result(self, jog_1, jog_2):
        if jog_1 == jog_2:
            return 'empate'

        if jog_1 != jog_2:
            if jog_1 == 'pedra':
                if jog_2 == 'tesoura':
                    return 'vitoria'
                else:
                    return 'derrota'
            if jog_1 == 'tesoura':
                if jog_2 == 'papel':
                    return 'vitoria'
                else:
                    return 'derrota'
            if jog_1 == 'papel':
                if jog_2 == 'pedra':
                    return 'vitoria'
                else:
                    return 'derrota'
