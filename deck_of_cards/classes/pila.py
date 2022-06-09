class Pila:
    def __init__(self, deck):
        self.cards = []
        self.cards.append(deck.cards.pop(0))

    def mostrar_ultima_carta(self):
        self.cards[len(self.cards)-1].card_info()
    
    def mostrar_cartas(self):
        for i in range(len(self.cards)):
            print(f"{i}:")
            self.cards[i].card_info()


