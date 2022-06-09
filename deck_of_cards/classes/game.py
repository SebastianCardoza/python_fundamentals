from card import Card
from player import Player
from deck import Deck
from pila import Pila

nPlayers = 0
deck = Deck()
pila = Pila(deck)
players = []
noWinner = True
player_turn = 0
next_player_steals_cards=0
# Welcome message and rules
print("Bienvenido a 8 Locos!")
print("REGLAS DEL JUEGO:")
print("1. Todos los jugadores comienzan con 4 cartas")
print("2. Cada jugador tira una carta que coincida con el valor o palo de la carta a tope de la pila")
print("3. En caso el jugador no tenga una carta que coincida podra coger una carta del mazo y pasara su turno")
print("4. Hay cartas que tienen efectos al tirarlas:")
print("   * 2:  El proximo jugador pierde el turno")
print("   * 11: El jugador actual repite el turno")
print("   * 12: El proximo jugador coge 2 cartas")
print("   * 13: El proximo jugador coge 3 cartas")
print("5. Gana el que se queda sin cartas")
print("\nQue gane el mejor!!!!")
# Select number of players
while (nPlayers < 2 or nPlayers > 4):
    nPlayers = int(input("Cuantos jugadores hay? Pueden jugar de 2 a 4 personas \n"))
# Create the player profile and hands
for i in range(nPlayers):
    name = input(f"Cual es el nombre del jugador {i+1}? \n")
    player = Player(i, name, deck)
    players.append(player)
# Mostrar tarjeta a tope del mazo
print("\nTarjeta a tope de la pila:")
pila.mostrar_ultima_carta()
print(" ")
while (noWinner):
    print(f"Mano de {players[player_turn].name}:")
    players[player_turn].mostrar_cartas()
    tarjeta_tirar=int(input("Que numero de carta quieres tirar?\n"))

    # Dependiendo de la carta que se tire se determina si pasa el turno, se cambia el sentido o se repite el turno
    turnFactor = players[player_turn].tirar_cartas(tarjeta_tirar-1, pila.cards, deck)

    # Si el turnFactor devuelve 3 o 4 esto significara que el siguiente jugador debe agarrar cartas
    if turnFactor == 3:
        turnFactor = 1
        next_player_steals_cards = 2
    elif turnFactor == 4:
        turnFactor = 1
        next_player_steals_cards = 3

    # Revisar si el jugador gano
    if len(players[player_turn].cards) == 0:
        noWinner = False
        print(f"El ganador es {players[player_turn].name}")
        break

    # Si no se repite el turno, sumale el turnFactor y si player_turn es mayor a lo que deberia restale el numero de jugadores
    if not turnFactor == 0:
        player_turn += turnFactor
        if player_turn > len(players) - 1:
            player_turn -= len(players)
    
    # El siguiente jugador roba 2 o 3 cartas si le corresponde
    if next_player_steals_cards != 0:
        players[player_turn].agarrar_cartas(deck, next_player_steals_cards)
        print(f"\n{players[player_turn].name} robo {next_player_steals_cards} cartas") 
        next_player_steals_cards = 0

    # Mostrar carta a tope del mazo
    print("\nTarjeta a tope del mazo:")
    pila.mostrar_ultima_carta()

    # Si las cartas en la pila son mayores a 10, se deben volver a barajear
    if len(pila.cards) >= 5:
        deck.get_cards(pila.cards)
    print(" ")
    
