jugador1 = input("Jugador 1, elige piedra, papel o tijera: ")   
jugador2 = input("Jugador 2, elige piedra, papel o tijera: ")

if jugador1 == jugador2:
    print("Empate")
if (jugador1) == "piedra" and jugador2 == "tijera":
    print(f"Jugador 1 gana con {jugador1}")
if (jugador1) == "tijera" and jugador2 == "papel":
    print(f"Jugador 1 gana con {jugador1}")
if (jugador1) == "papel" and jugador2 == "piedra":
    print(f"Jugador 1 gana con {jugador1}")
if (jugador2) == "piedra" and jugador1 == "tijera":
    print(f"Jugador 2 gana con {jugador2}")
if (jugador2) == "tijera" and jugador1 == "papel":
    print(f"Jugador 2 gana con {jugador2}")
if (jugador2) == "papel" and jugador1 == "piedra":
    print(f"Jugador 2 gana con {jugador2}")