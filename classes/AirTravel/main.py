from airtravel import Flight
from airtravel import Aircraft

possible_flights = {'joke':, 'AP564', '23' , 'casa']
for flight in possible_flights:
    try:
        result = Flight(flight)
        print(result)
    except ValueError as Erro:
        print(Erro)

aircraft = Aircraft('AZUL','487', 21, 7)
model = aircraft.model()
registration = aircraft.registration()
seats = aircraft.seating_plan()
print(seats, model, registration)
