import random


# suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
# values = [10, 9, 8, 7, 6, 11, 12, 13, 1]
# deck = {}

# for i in values:
#     for x in suits:
#         deck.append(x + " of " + i)
    
class Spar:
    
    def __init__(self, score, deck):
        self.score = score
        self.deck = deck
        
    
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
                    deck[x] = i 
        return deck 
        
    def deal(self):
        self.deck = deck()
        shuffledDeck = random.shuffle(deck)
        
        for player in playersList:
            amountOfCardsPerTrick = 1
            while amountOfCardsPerTrick <= 5:
                player.cards.append(shuffledDeck.pop)
                amountOfCardsPerTrick += 1  
            
    def game():
        
            
            
class Player: