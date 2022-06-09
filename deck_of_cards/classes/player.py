class Player:
    def __init__(self, number, name, deck):
        self.number = number
        self.name = name
        self.cards = []
        self.agarrar_cartas(deck, 4)

    def agarrar_cartas(self, deck, number):
        for i in range(number):
            self.cards.append(deck.cards.pop(0))

    def tirar_cartas(self, card, pila, deck):
        
        ultima_carta = pila[len(pila)-1]
        # Si la carta es del mismo palo o el mismo numero, se acepta de otra manera se vuelve a pedir otra carta
        if ultima_carta.palo == self.cards[card].palo or ultima_carta.numero == self.cards[card].numero:
            pila.append(self.cards.pop(card))
            # Si tiran 11 se repite el turno
            if pila[len(pila)-1].numero == 11:
                return 0
            # Si tiran 2 se salta un turno
            elif pila[len(pila)-1].numero == 2:
                return 2
            # Si tiran 12 el siguiente jugador debera coger 2 cartas
            elif pila[len(pila)-1].numero == 12:
                return 3
            # Si tiran 13 el siguiente jugador debera coger 3 cartas
            elif pila[len(pila)-1].numero == 13:
                return 4
            # De otra manera se continua normal
            else:
                return 1
        else:
            print("Carta tirada invalida")
            card = int(input("Escribe el numero de una carta valida o escribe '99' si deseas agarrar una carta y pasar el turno \n"))
            if card == 99:
                self.agarrar_cartas(deck, 1)
                return 1
            else:
                return self.tirar_cartas(card-1, pila, deck)
    
    def mostrar_cartas(self):
        for i in range(len(self.cards)):
            print(f"{i+1}: ")
            self.cards[i].card_info() 
