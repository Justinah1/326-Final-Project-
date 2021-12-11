import random
    
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
    
        face = [14, 13, 12, 11, 10, 9, 8, 7, 6]
        suits = ["Hearts","Spades","Clubs","Diamonds"]
        self.deck = []
        for i in face:
            for x in suits:
                if x != "Spades" and i != "A":
                    self.deck.append(Card(i, x))
        return self.deck 
        
    def deal(self):
        shuffledDeck = random.shuffle(self.deck())
        
        for player in self.playersList:
            amountOfCardsPerTrick = 1
            while amountOfCardsPerTrick <= 5:
                player.cards.append(shuffledDeck.pop())
                amountOfCardsPerTrick += 1  
                
    def setCurrCard(self, player):
        self.currCard = player.playTurn()
            
    def game(self):
        turn = -1
        round = 0
        player = None
        
        if round == 0:
            self.setCurrCard(self.playersList[0])
            round += 1
            turn += 1
        
        while round <= 5:
            turn += 1
            player = self.playersList[turn % len(self.playersList)]
            if len(self.playersList[0].cards) > 0:
                
                player.playTurn() 
        
class Card:
    def __init(self, face, suit):
        self.suit = suit
        self.face = face       
    
    def __repr__(self):
        print(f"Card({self.suit},{self.face}")     
            
class Player:
    def __init__(self, name, currCard, cards = []):
        self.name = name
        self.cards = cards
        self.currCard = currCard
        
    def playTurn(self):
       
        for card in self.cards:
            print(card)
        first_card = int(input("Select a card (Using a number)"))
        self.currCard = self.cards.pop(first_card - 1)
        return self.currCard
    
class ComputerPlayer:
    def __init__(self, name, currCard, cards = []):
        self.name = name
        self.cards = cards
        self.currCard = currCard
        
    def getCurrCard(self, currCard):
        self.currCard = currCard
        
    def compTurn(self):
        highestFace = 0
        lowestFace = 15
        cardToDeal = Card()
        goodHand = []
        hasCard = False
        
        for card in self.cards:
           if card.suit == self.currCard.suit:
               goodHand.append(card)
               hasCard = True
        
        if hasCard == True:
            for card in goodHand:
                if card.face > highestFace:
                    cardToDeal = card
                    highestFace = card.face
        else:
            goodHand = self.cards
            for card in goodHand:
               if card.face < lowestFace:
                   cardToDeal = card
                   lowestFace = card.face
        return cardToDeal
