import random
from card import Card

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append(Card( s , i , str_val ) )
        # Barajear las cartas nomas se inicie
        self.mix_cards()

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def mix_cards(self):
        random.shuffle(self.cards)

    def get_cards(self, pila):
        for i in range(len(pila)-1):
            self.cards.append(pila.pop(0))
        print(f"Numero de cartas en pila {len(pila)}")
