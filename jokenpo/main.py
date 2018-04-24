#Program to execute the class
from jokenpov2 import *

jog_1 = input("Insira a opção do jogador 1")
jog_2 = input("Insira a opção do jogador 2")

game = Jokenpo(jog_1, jog_2)
resultado = game.result(jog_1, jog_2)
print("O jogador 1 {}".format(resultado))
