import random


class BlackJack :

    _deck = [
        2,3,4,5,6,7,8,9,10,
        2,3,4,5,6,7,8,9,10,
        2,3,4,5,6,7,8,9,10,
        2,3,4,5,6,7,8,9,10,
        "J", "K", "A", "Q",
        "J", "K", "A", "Q",
        "J", "K", "A", "Q",
        "J", "K", "A", "Q"
    ]
    _hand_of_player = []
    _hand_of_dealer = []

    def __init__(self):
        print("init game")


    def deal_hand(self, turn) :
        card = random.choice( len( self._deck ) - 1 )
        turn.append(card)
        self._deck.remove(card)


    def total_each_hand(self, turn) :
        total = 0
        face = ["J", "K", "A", "Q"]

        for card in turn :

            if card in range(1, 11) :
                total = total + card

            if card in face : 
                total = total + 1
    
            if total > 11 :
                total = total + 1
            else :
                total = total + 11

        return total


if __name__ == "__main__" :
    pass