# create a jokenpo class
import random

class Jokenpo:
    def __init__(self, jog_1, jog_2):
        self.jog_1 = jog_1
        self.jog_2 = jog_2

    def play(self):
        if self.jog_2 == self.jog_1:
            return 'Draw'

        elif self.jog_2 != self.jog_1:
            if self.jog_1 == 'stone':
                if self.jog_2 == 'scissor':
                    return 'Win'
                else:
                    return 'Lose'
            elif self.jog_1 == 'scissor':
                if self.jog_2 == 'paper':
                    return 'Win'
                else:
                    return 'Lose'
            else:
                if self.jog_2 == 'stone':
                    return 'Lose'
                else:
                    return 'Win'


test = ['stone', 'scissor', 'paper']

x = random.choice(test)
y = random.choice(test)
result = Jokenpo(x, y)
winner = result.play()
print('O primeiro jogador escolheu {}, o segundo {} o segundo jogador {}'.format(x, y, winner))
