from airtravel import Flight
possible_flights = ['joke', 'AP564', '23' , 'casa']
for flight in possible_flights:
    try:
        result = Flight(flight)
        print(result)
    except ValueError as Erro:
        print(Erro)
