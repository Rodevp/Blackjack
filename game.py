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
    _player_in = True
    _dealer_in = True

    def __init__(self):
        print("init game")


    def deal_hand(self, turn) :
        card = random.choice( self._deck )
        turn.append(card)
        self._deck.remove(card)


    def total_each_hand(self, turn) :
        total = 0
        face = ["J", "K", "A", "Q"]

        for card in turn :

            if card in range(1, 11) :
                total = total + card

            if card in face : 
                total = total + 10
    
            if total > 11 :
                total = total + 1
            else :
                total = total + 11

        return total

    
    def reveal_hand_of_dealer(self) :

        if len(self._hand_of_dealer) == 2 :
            return self._hand_of_dealer[0]
        
        if len(self._hand_of_dealer) > 2 :
            return self._hand_of_dealer[0], self._hand_of_dealer[1] 


    def menu(self) :

        while self._dealer_in or self._player_in :
            print(f"Hand of dealer {self.reveal_hand_of_dealer()} ")
            print(f"Your total of in the hand is: You have {self._hand_of_player} total: {self.total_each_hand(self._hand_of_player)}")

            if self._player_in :
                stay_or_hit = input("1: Stay\n2: Hit\n")
            
            if self.total_each_hand(self._hand_of_player) > 16 :
                self._dealer_in = False 
            else :
                self.deal_hand(self._hand_of_dealer)

            if stay_or_hit == '1' :
                self._player_in = False
            else : 
                self.deal_hand(self._hand_of_player)

            if self.total_each_hand(self._hand_of_player) >= 21 : break

            if self.total_each_hand(self._hand_of_dealer) >= 21 : break


    def print_you_lose(self) :
        print(f"You have: {self._hand_of_player} equal {self.total_each_hand(self._hand_of_player)}")
        print(f"dealer have {self._hand_of_dealer} equal {self.total_each_hand(self._hand_of_dealer)}")
        print("YOU LOSE!!! :(") 


    def print_you_win(self) :
        print(f"You have: {self._hand_of_player} equal {self.total_each_hand(self._hand_of_player)}")
        print(f"dealer have {self._hand_of_dealer} equal {self.total_each_hand(self._hand_of_dealer)}")
        print("YOU WIN!!! :D")
    

    def start(self) :

        for _ in range(2) :
            self.deal_hand(self._hand_of_dealer)
            self.deal_hand(self._hand_of_player)

        self.menu()

        if self.total_each_hand(self._hand_of_player)  == 21 : self.print_you_win()
        if self.total_each_hand(self._hand_of_dealer)  == 21 : self.print_you_lose()
        
        if self.total_each_hand(self._hand_of_dealer)  > 21 : self.print_you_win()
        if self.total_each_hand(self._hand_of_player)  > 21 : self.print_you_lose()

        if 21 - self.total_each_hand(self._hand_of_dealer) > 21 - self.total_each_hand(self._hand_of_player) : self.print_you_win()
        if 21 - self.total_each_hand(self._hand_of_dealer) < 21 - self.total_each_hand(self._hand_of_player) : self.print_you_lose()




if __name__ == "__main__" :
    game = BlackJack()
    game.start()