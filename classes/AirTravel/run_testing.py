from airtravel import *
from pprint import pprint as pp


f = Flight("PS3453", Aircraft("AZUL","BUS457",num_rows = 10, num_seats_per_row=5))
#g = Aircraft("AZUL","BUS457",num_rows = 22, num_seats_per_row=5)
#print(g.model())
try:
    f.allocate_seat("13F",'Lucas')
except ValueError as erro:
    print(erro)
