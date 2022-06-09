class Card:

    def __init__( self , suit , point_val , string_val ):
        
        self.palo = suit
        self.string_val = string_val
        self.numero = point_val

    def card_info(self):
        print(f"{self.numero} of {self.palo}")