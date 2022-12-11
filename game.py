import random


class BlackJack :

    _deck = [2,3,4,5,6,7,8,9,10, "J", "K", "A", "Q"]
    _hand_of_player = []
    _hand_of_dealer = []

    def __init__(self):
        print("init game")


    def deal_hand(self, turn) :
        card = random.choice( len( self._deck ) - 1 )
        turn.append(card)
        self._deck.remove(card)
        




if __name__ == "__main__" :
    pass