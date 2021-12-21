<<<<<<< HEAD
""" This is a card game called spar. Spar is a card game between a human player and a computer 
        player with each player being dealt 5 cards. The goal is to match the suite of the current card
"""

from argparse import ArgumentParser
import sys
=======
>>>>>>> 8dc3fcf1eb5883f90ea308ead0af8c4d45777e56
import random
from random import randrange


# suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
# values = [10, 9, 8, 7, 6, 11, 12, 13, 1]
# deck = {}

# for i in values:
#     for x in suits:
#         deck.append(x + " of " + i)
    
class Spar:
    """
    The spar class should have the dealing of cards, the deck, and the game itself
    
    Attributes:
        score(int): Used to keep track of scores after each round
        deck(list): The list that contains the suits and faces of the cards
        currCard(str): The current on the table
    """
    
<<<<<<< HEAD
    def __init__(self, score, deck = [], playersList = [], currCard = None):
        """sets the attributes
        
        Args:
            score(int): Used to keep track of scores after each round
            deck(list): The list that contains the suits and faces of the cards
            currCard(str): The current on the table
        """
=======
    def __init__(self, score, deck, playersList, currCard = None):
>>>>>>> 8dc3fcf1eb5883f90ea308ead0af8c4d45777e56
        self.score = score
        self.deck = deck
        # self.playersList = playersList
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
<<<<<<< HEAD
        """ This method deals the cards for the players
        """
        shuffledDeck = self.newDeck()
        random.shuffle(shuffledDeck)
=======
        shuffledDeck = random.shuffle(self.deck())
>>>>>>> 8dc3fcf1eb5883f90ea308ead0af8c4d45777e56
        
        for player in self.playersList:
            amountOfCardsPerTrick = 1
            while amountOfCardsPerTrick <= 5:
                player.cards.append(shuffledDeck.pop())
                amountOfCardsPerTrick += 1  
                
    def setCurrCard(self, player):
        """ This method sets the current card on the table
        
        Args:
            player(str):
        """
        self.currCard = player.playTurn()
        
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
            
<<<<<<< HEAD
    def game(self): 
        """This is the method that describes and sets the game and how the game will be played
        """
=======
    def game(self):
        
        
>>>>>>> 8dc3fcf1eb5883f90ea308ead0af8c4d45777e56
        compScore = 0
        round = 0
        trick = 0
        player = None
        
        compTrick = False
        
        while round < 5:
        
            if trick == 0:
                self.setCurrCard(self.playersList[0])
                compCardPlayed = self.playerList[1].compTurn()
                if compCardPlayed.suit == self.currCard.suit:
                    if compCardPlayed.face > self.currCard.face:
                        compTrick = True
                        
                trick += 1
                
            
            while trick < 5:
                
                if compTrick == True:
                    self.currCard = self.playersList[1].compTurn()
                    
                    playedCard = self.playersList[0].compTurn()
                    
                    if playedCard.suit == self.currCard.suit:
                        if playedCard.face > self.currCard.face:
                            if trick == 4:
                                self.score += self.scoring(playedCard.face)
                            compTrick = False
                    else:
                        compTrick = True
                        if trick == 4:
                            compScore += self.scoring(compCardPlayed.face)
                else:
                    self.currCard = self.playersList[0].playTurn()
                    
                    compCardPlayed = self.playersList[1].compTurn()
                    
                    if compCardPlayed.suit == self.currCard.suit:
                        if compCardPlayed.face > self.currCard.face:
                            if trick == 4:
                                compScore += self.scoring(compCardPlayed.face)
                            compTrick = True
                    else:
                        compTrick = False
                        if trick == 4:
                            self.score += self.scoring(playedCard.face)
                            
            round += 1
            
            
            
          
            
        
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
<<<<<<< HEAD
        return (f"{self.suit},{self.face}")        
         
=======
        """Create a method using __repr__ to get a printable representation of the object
                Returns:
                    f-string
        """
        print(f"Card({self.face},{self.suit}")     
>>>>>>> 8dc3fcf1eb5883f90ea308ead0af8c4d45777e56
            
class Player:
    """Manages player turn
        Attributes:
            name(str): name
            cards(str): deck of cards
            currCard(str): current card trick
            
    """
    def __init__(self, name, currCard, cards = []):
        self.name = name
        self.cards = cards
        self.currCard = currCard
        
<<<<<<< HEAD
    def dealCards(self, card):
        self.cards.append(card)
    
    def getCurrCard(self, currCard):
        self.currCard = currCard
        
        
=======
>>>>>>> 8dc3fcf1eb5883f90ea308ead0af8c4d45777e56
    def playTurn(self):
        """Prints out player cards

        Returns:
            currCard(str): returns current card trick 
        """
       
        for card in self.cards:
            print(card)
        first_card = int(input("Select a card (Using a number)"))
        self.currCard = self.cards.pop(first_card - 1)
        return self.currCard
    
class ComputerPlayer:
    """Manages Computer's turn
    """
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
