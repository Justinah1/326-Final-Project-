import random
from random import randrange


# suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
# values = [10, 9, 8, 7, 6, 11, 12, 13, 1]
# deck = {}

# for i in values:
#     for x in suits:
#         deck.append(x + " of " + i)
    
class Spar:
    
    def __init__(self, score, deck, playersList, currCard = None):
        self.score = score
        self.deck = deck
        self.playersList = playersList
        self.currCard = currCard
        
    
    def deck(self):
        """This method creates and sets the deck of cards 

        Returns:
        deck [str]: returns all deck card values
    """
    
        face = ["K","Q","J","A", "6", "7", "8", "9", "10"]
        suits = ["Hearts","Spades","Clubs","Diamonds"]
        self.deck = {}
        for i in face:
            for x in suits:
                if x is not "Spades" and i is not "A":
                    self.deck[x] = i 
        return self.deck 
        
    def deal(self):
        shuffledDeck = random.shuffle(self.deck())
        cards =[]
        
        for player in self.playersList:
            amountOfCardsPerTrick = 1
            while amountOfCardsPerTrick <= 5:
                x = shuffledDeck
                cards.append(x)
                amountOfCardsPerTrick += 1  
            
    def game(self):
        turn = -1
        player = None
        while len(self.playersList[0].cards) > 0:
            turn += 1
            player = self.playersList[turn % len(self.playersList)]
            if 
        
            
            
class Player:
    def __init__(self, name, cards = []):
        self.name = name
        self.cards = cards
        
    def playTurn(self,player):
        if self.currCard == None:
            print()
        while True:
            try:
                player_input = int(input(f"Enter a suit between  {p1}:"))
                if player_input < 20 or player_input > 30:
                    print("Out of range")
                else:
                    p1_num = player_input + randrange(10)
                    print(p1_num)
                if p1_num > p2_num:
                    print("p1 wins")
                elif p2_num > p1_num:
                    print("p2 wins")
                else:
                    print("It's a tie")
            except ValueError:
                print("Not a valid entry")