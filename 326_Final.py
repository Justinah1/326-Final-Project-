""" This is a card game called spar. Spar is a card game between a human player and a computer 
        player with each player being dealt 5 cards. The goal is to match the suite of the current card
"""

from argparse import ArgumentParser
import sys
import random
from termcolor import colored

    
class Spar:
    """
    The spar class should have the dealing of cards, the deck, and the game itself
    
    Attributes:
        score(int): Used to keep track of scores after each round
        deck(list): The list that contains the suits and faces of the cards
        currCard(str): The current on the table
    """
    
    def __init__(self, score, deck = [], playersList = [], currCard = None):
        """sets the attributes
        
        Args:
            score(int): Used to keep track of scores after each round
            deck(list): The list that contains the suits and faces of the cards
            currCard(str): The current on the table
        """
        self.score = score
        self.deck = deck
        # self.playersList = playersList
        self.currCard = currCard
        
    
    def newDeck(self):
        """This method creates and sets the deck of cards 
        
        Returns:
            deck [str]: returns all deck card values
    """
    
        face = [14, 13, 12, 11, 10, 9, 8, 7, 6]
        suits = ["Hearts","Spades","Clubs","Diamonds"]
        deck = []
        for i in face: # Goes through the face list
            for x in suits: # Goes through the suits list
                if x != "Spades" and i != 14:
                    deck.append(Card(i, x))
        return deck # returns a list of tuples
        
    def deal(self):
        """ This method deals the cards for the players
        """
        shuffledDeck = self.newDeck() # makes a deck
        random.shuffle(shuffledDeck) # shuffles the list of tuples (cards)
        
        for player in self.playersList: 
            amountOfCardsPerTrick = 1
            while amountOfCardsPerTrick <= 5: # setting the max number of cards per trick
                player.dealCards(shuffledDeck.pop())
                amountOfCardsPerTrick += 1  
                
    def setCurrCard(self, player):
        """ This method sets the current card on the table
        
        Args:
            player(str):
        """
        self.currCard = player.playTurn()   # prints out player's cards
                                            # and also sets the current card
                                            
        player.getCurrCard(self.currCard)   # sets player's current card within
                                            # the spar class
        
    def scoring(self, num):
        """ This method is used to keep track of the scores
        
        Args:
            num():
            
        Returns:
        
        """
        if num == 6:
            return 3
        elif num == 7:
            return 2
        else:
            return 1
            
    def game(self): 
        """This is the method that describes and sets the game and how the game will be played
        """
        compScore = 0   
        round = 0
        trick = 0
        
        self.deal() # deals cards out to the players
        
        compTrick = False
        
        while round < 5:
        
            if trick == 0:
                print("TRICK 1:")
                self.setCurrCard(self.playersList[0]) #sets the spar class' current card
                print("CURRENT CARD ON TABLE: " + str(self.currCard)) # displays what it is
                compCardPlayed = self.playersList[1].compTurn() # Computer player's cards are shown and uses a card
                
                self.playersList[1].getCurrCard(self.currCard)
                
                if compCardPlayed.suit == self.currCard.suit:
                    if compCardPlayed.face > self.currCard.face:
                        compTrick = True
                        print("**COMPUTER WON TRICK**")
                else:
                    print("**PLAYER WON TRICK**")        
                trick += 1
                
            
            while trick < 5:
                print("TRICK " + str(trick + 1))
                if compTrick == True:
                    self.currCard = self.playersList[1].compTurn()
                    print("CURRENT CARD ON TABLE: " + str(self.currCard))
                    playedCard = self.playersList[0].playTurn()
                    
                    
                    if playedCard.suit == self.currCard.suit:
                        if playedCard.face > self.currCard.face:
                            if trick == 4:
                                self.score += self.scoring(playedCard.face)
                            compTrick = False
                            print("**PLAYER WON TRICK**")
                    else:
                        compTrick = True
                        print("**COMPUTER WON TRICK**")
                        if trick == 4:
                            compScore += self.scoring(compCardPlayed.face)
                else:
                    self.currCard = self.playersList[0].playTurn()
                    print("CURRENT CARD ON TABLE: " + str(self.currCard))
                    compCardPlayed = self.playersList[1].compTurn()
                    
                    if compCardPlayed.suit == self.currCard.suit:
                        if compCardPlayed.face > self.currCard.face:
                            if trick == 4:
                                compScore += self.scoring(compCardPlayed.face)
                            compTrick = True
                            text = colored("**COMPUTER WON TRICK**", 'red', attrs=['reverse', 'blink']) 
                            print(text)
                    else:
                        compTrick = False
                        print("**PLAYER WON TRICK**")
                        if trick == 4:
                            self.score += self.scoring(playedCard.face)
                trick += 1
                            
            round += 1
            self.deal()
                   
class Card:
    """Creates cards for class and prints values
    Attributes:
        suit(str): suit of cards
        face(str): face of cards
    """
    def __init__(self, face, suit):
        self.suit = suit
        self.face = face
    
    def __repr__(self):
        """Create a method using __repr__ to get a printable representation of the object
        
        Returns:
            f-string
        """ 
        return (f"{self.suit},{self.face}")        
         
            
class Player:
    """Manages player turn
    
    Attributes:
        name(str): name
        cards(str): deck of cards
        currCard(str): current card trick
            
    """
    def __init__(self, name, currCard = Card(14, "Hearts"), cards = []):
        self.name = name
        self.cards = cards
        self.currCard = currCard
        
    def dealCards(self, card):
        self.cards.append(card)
    
    def getCurrCard(self, currCard):
        self.currCard = currCard
        
        
    def playTurn(self):
        """Prints out player cards

        Returns:
            currCard(str): returns current card trick 
        """
       
        print("PLAYER HAND:")
        for card in self.cards:
            print(str(self.cards.index(card) + 1) + ") " + str(card)) 
        
        print("")
        
        first_card = int(input("Select a card to play(Using a number): "))
        self.currCard = self.cards.pop(first_card - 1)
        print("PLAYED CARD:" + str(self.currCard))
        print("")
        return self.currCard
    
class ComputerPlayer:
    """Manages Computer's turn
    
    Attributes:
    name(str): the name of the computer player?
    currCard(): current card with a default value of Card(14, "Hearts")
    cards(list):
    """
    def __init__(self, name, currCard = Card(14, "Hearts"), cards = []):
        self.name = name
        self.cards = cards
        self.currCard = currCard
    
    def dealCards(self, card):
        self.cards.append(card)
        
    def getCurrCard(self, currCard):
        self.currCard = currCard
        
    def compTurn(self):
        highestFace = 0
        lowestFace = 15
        cardToDeal = Card(14, "Hearts")
        goodHand = []
        hasCard = False
        
        print("COMP HAND:")
        for card in self.cards:
            print(str(self.cards.index(card) + 1) + ") " + str(card))
        
        for card in self.cards:
           if card.suit == self.currCard.suit:
               goodHand.append(card)
               hasCard = True
        
        if hasCard == True:
            for card in goodHand:
                if card.face > highestFace:
                    cardToDeal = self.cards.pop(self.cards.index(card))
                    highestFace = card.face
        else:
            goodHand = self.cards
            for card in goodHand:
               if card.face < lowestFace:
                   cardToDeal = self.cards.pop(self.cards.index(card))
                   lowestFace = card.face
        print("COMPUTER CARD PLAYED: " + str(cardToDeal))
        print("")
        return cardToDeal

def main(name, computer_player):
    """
    """
    players = [Player(name), ComputerPlayer(computer_player)]
   
    game = Spar(score = 0, playersList= players)
    game.game()


def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("names", nargs="*", help="player names")
    parser.add_argument("-c", "--computer_player", action="store_true",
                        help="add a computer player")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.names, args.computer_player)
    
    
#Test the code in terminal with this example (if mac): python3 filename player_name -c