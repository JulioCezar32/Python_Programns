
class Stack():

    def __init__(self, size):
        self.size = size
        self.stone = []
        self.generate_stone()

    def generate_stone(self):

        self.stone = [x for x in range(1, self.size + 1)]

    def receive_stone(self, stone_received):
        if self.stone[-1] <= stone_received:
            self.stone.append(stone_received)
            return 0
        else:
            return 1

##remover item de um vetor nulo retorna um erro, é melhor tratar com if ou com um exception

    def remove_stone(self):
        self.removed_item = self.stone[-1]
        del self.stone[-1]
        return self.removed_item
