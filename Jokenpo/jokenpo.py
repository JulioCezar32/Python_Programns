# create a jokenpo class


class Jokempo:

    def __init__(self, jog_1, jog_2):
        self.jog_1 = jog_1
        self.jog_2 = jog_2

    def stone(self):
        if self.jog_2 == 'stone':
            return 'Draw'
        elif self.jog_2 == 'scissor':
            return 'Win'
        elif self.jog_2 == 'paper':
            return 'Lose'

    def paper(self):
        if self.jog_2 == 'stone':
            return 'Win'
        elif self.jog_2 == 'scissor':
            return 'Lose'
        elif self.jog_2 == 'paper':
            return 'Draw'

    def scissor(self):
        if self.jog_2 == 'stone':
            return 'Lose'
        elif self.jog_2 == 'scissor':
            return 'Draw'
        elif self.jog_2 == 'paper':
            return 'Win'
