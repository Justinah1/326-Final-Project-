""" This is a card game called spar. Spar is a card game between a human player and a computer 
        player with each player being dealt 5 cards. The goal is to match the suite of the current card
"""

from argparse import ArgumentParser
import sys
import random

    
class Spar:
    """
    The spar class should have the dealing of cards, the deck, and the game itself
    
    Attributes:
        score(int): Used to keep track of scores after each round
        deck(list): The list that contains the suits and faces of the cards
        playersList(list): The list of players
        currCard(str): The current on the table
    """
    
    def __init__(self, score, deck = [], playersList = [], currCard = None):
        """sets the attributes
        
        Args:
            score(int): Used to keep track of scores after each round
            deck(list): The list that contains the suits and faces of the cards
            playersList(list): The list of players
            currCard(str): The current on the table
        """
        self.score = score
        self.deck = deck
        self.playersList = playersList
        self.currCard = currCard
        
    
    def newDeck(self):
        """This method creates and sets the deck of cards 
        
        Returns:
            deck (str): returns all deck card values
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
        """ This method deals and shuffles the cards for the players
        
        Side effects:
            It modifies the card hand of player and computer objects
        """
        shuffledDeck = self.newDeck() # makes a deck
        random.shuffle(shuffledDeck) # shuffles the list of tuples (cards)
        
        for player in self.playersList: 
            amountOfCardsPerTrick = 1
            while amountOfCardsPerTrick <= 5: # setting the max number of cards per trick
                player.dealCards(shuffledDeck.pop())
                amountOfCardsPerTrick += 1 
                
                 
                
    def setCurrCard(self, player):
        """ This method sets the current card on the table. Allows the players
            to play their card and is only used for the first trick.
        
        Args:
            player(object): A player object
        """
        self.currCard = player.playTurn()   # prints out player's cards
                                            # and also sets the current card
                                            
        player.getCurrCard(self.currCard)   # sets player's current card within
                                            # the spar class
                                            
                                            
        
    def scoring(self, num):
        """ This method is used to keep track of the scores
        
        Args:
            num(int): The face value of the last card
            
        Returns:
            int: The scores
        """
        if num == 6:
            return 3
        elif num == 7:
            return 2
        else:
            return 1
            
            
            
    def game(self): 
        """This is the method that describes and sets the game and how the game will be played
        
        Side effects:
            prints to stdout
            modifies the score attribute
            modifies currCard after each trick
            modifies the deck and player's hand 
        """
        overallCompScore = 0   
        round = 0
        trick = 0
        
        self.deal() # deals cards out to the players
        
        compTrick = False
        
        while round < 3:
            print("====ROUND " + str(round + 1) + "====")
            
            if trick == 0:
                print("---TRICK 1---")
                self.setCurrCard(self.playersList[0]) #sets the spar class' current card
                print("CURRENT CARD ON TABLE: " + str(self.currCard)) # displays what it is
                print("")
                
                self.playersList[1].getCurrCard(self.currCard) # computer gets the card on the table
                compCardPlayed = self.playersList[1].compTurn() # Computer player's cards are shown and uses a card
                
                if compCardPlayed.suit == self.currCard.suit:
                    if compCardPlayed.face > self.currCard.face:
                        compTrick = True
                        print("**COMPUTER WON TRICK**----------------")
                        print("")
                    else:
                        print("**PLAYER WON TRICK**----------------") 
                        print("") 
                else:
                    print("**PLAYER WON TRICK**----------------") 
                    print("")       
                trick += 1
                
            
            while trick < 5:
                print("---TRICK " + str(trick + 1) + "---")
                if compTrick == True: #computer won previous trick so it goes again
                    self.currCard = self.playersList[1].compTurn() #computer plays card
                    print("CURRENT CARD ON TABLE: " + str(self.currCard))
                    print("")
                    playedCard = self.playersList[0].playTurn() #player plays a card
                    
                    
                    if playedCard.suit == self.currCard.suit: # check if player card has matching suit
                        if playedCard.face > self.currCard.face: # check if player card has better face
                            compTrick = False # set false if player card wins
                            print("**PLAYER WON TRICK**----------------")
                            print("")
                            if trick == 4: # if 4th trick then get score for player 
                                self.score += self.scoring(playedCard.face)
                                tempPlayerScore = self.scoring(playedCard.face)
                                print("PLAYER EARNED: " + str(tempPlayerScore) + " POINTS")
                                print("")
                        else:
                            compTrick = True # set true if player card does not have matching suit
                            print("**COMPUTER WON TRICK**----------------")
                            print("")
                            if trick == 4:
                                overallCompScore += self.scoring(compCardPlayed.face)
                                tempCompScore = self.scoring(compCardPlayed.face)
                                print("COMPUTER EARNED: " + str(tempCompScore) + " POINTS")
                                print("")
                    else:
                        compTrick = True # set true if player card does not have matching suit
                        print("**COMPUTER WON TRICK**----------------")
                        print("")
                        if trick == 4:
                            overallCompScore += self.scoring(compCardPlayed.face)
                            tempCompScore = self.scoring(compCardPlayed.face)
                            print("COMPUTER EARNED: " + str(tempCompScore) + " POINTS")
                            print("")
                else:
                    self.currCard = self.playersList[0].playTurn()
                    playedCard = self.currCard
                    print("CURRENT CARD ON TABLE: " + str(self.currCard))
                    print("")
                    self.playersList[1].getCurrCard(self.currCard) #gives the computer the card on the table
                    compCardPlayed = self.playersList[1].compTurn() # computer plays card
                    
                    if compCardPlayed.suit == self.currCard.suit:
                        if compCardPlayed.face > self.currCard.face:
                            compTrick = True
                            print("**COMPUTER WON TRICK**----------------")
                        else:
                            compTrick = False
                            print("**PLAYER WON TRICK**----------------")
                            print("")
                            if trick == 4:
                                self.score += self.scoring(playedCard.face)
                                tempPlayerScore = self.scoring(playedCard.face)
                                print("PLAYER EARNED: " + str(tempPlayerScore) + " POINTS")
                                print("")
                    else:
                        compTrick = False
                        print("**PLAYER WON TRICK**----------------")
                        print("")
                        if trick == 4:
                            self.score += self.scoring(playedCard.face)
                            tempPlayerScore = self.scoring(playedCard.face)
                            print("PLAYER EARNED: " + str(tempPlayerScore) + " POINTS")
                            print("")
                trick += 1
                            
            round += 1
            trick = 0
            compTrick = False
            self.deal()
            
        if self.score > overallCompScore:
            print("YOU BEAT THE COMPUTER!!")
            print("PLAYER SCORE:" + str(self.score))
            print("COMPUTER SCORE: " + str(overallCompScore))
        elif self.score == overallCompScore:
            print("YOU TIED!!!!")
            print("PLAYER SCORE:" + str(self.score))
            print("COMPUTER SCORE: " + str(overallCompScore))
        else:
            print("YOU LOST TO THE COMPUTER!!")
            print("COMPUTER SCORE: " + str(overallCompScore))
            print("PLAYER SCORE:" + str(self.score))
            
                   
class Card:
    """Creates cards for class and prints values
    
    Attributes:
        suit(str): suit of cards
        face(str): face of cards
    """
    def __init__(self, face, suit):
        """sets attributes
        
        Args:
            suit(str): suit of cards
            face(str): face of cards
        """
        self.suit = suit
        self.face = face
    
    
    
    def __repr__(self):
        """This method is used to get a formal representation of the object
        
        Returns:
            f-string: suit and face
        """ 
        return (f"{self.suit},{self.face}")        
         
            
            
            
class Player:
    """Manages player turn
    
    Attributes:
        name(str): name of player
        currCard(object): a card object with a default value of Card(14, "Hearts")
        cards(list):list of cards
            
    """
    def __init__(self, name, currCard = Card(14, "Hearts"), cards = []):
        """sets the attributes
        
        Args:
            name(str): name of player
            currCard(object): a card object with a default value of Card(14, "Hearts")
            cards(list):list of cards
        """
        self.name = name
        self.cards = cards
        self.currCard = currCard
        
        
        
    def dealCards(self, card):
        """Deals the card to the player
        
        Args:
            card(object): A card object
        """
        self.cards.append(card)
    
    
    def getCurrCard(self, currCard):
        """Gets the current card on the table for the player
        
        Args:
            currCard(object): This a current card object
        """
        self.currCard = currCard
        
        
    def playTurn(self):
        """Prints out player cards

        Returns:
            currCard(object): returns current card trick 
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
        name(str): name of computer player
        currCard(object): a card object with a default value of Card(14, "Hearts")
        cards(list): list of cards
    """
    def __init__(self, name, currCard = Card(14, "Hearts"), cards = []):
        """sets the attributes
        
        Args:
            name(str): name of computer player
            currCard(object): a card object with a default value of Card(14, "Hearts")
            cards(list): list of cards
        """
        self.name = name
        self.cards = cards
        self.currCard = currCard
    
    
    
    def dealCards(self, card):
        """Deals the card to the computer player
        
        Args:
            card(object): A card object
        """
        self.cards.append(card)
        
        
        
    def getCurrCard(self, currCard):
        """Gets the current card on the table for the computer player
        
        Args:
            currCard(object): This a current card object
        """
        self.currCard = currCard
        
        
        
    def compTurn(self):
        """Manages the computer player's turn to go
        
        Returns:
            cardToDeal(object): A card object that the computer plays
            
        Side effects:
            prints to stdout
            modifies cardToDeal
        """
        highestFace = 0
        lowestFace = 15
        cardToDeal = Card(14, "Hearts")
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
            self.cards.pop(self.cards.index(cardToDeal))
        else:
            goodHand = self.cards
            for card in goodHand:
               if card.face < lowestFace:
                   cardToDeal = card
                   lowestFace = card.face
            self.cards.pop(self.cards.index(cardToDeal))
        print("COMPUTER CARD PLAYED: " + str(cardToDeal))
        print("")
        return cardToDeal

def main(name, computer_player):
    """ sets up and play a game of spar
    
    Args:
        name(str): name of human player
        computer_player(str): computer player
        
    Side effects:
        writes to stdout
    """
    players = [Player(name), ComputerPlayer(computer_player)]
   
    game = Spar(score = 0, playersList= players)
    game.game()


def parse_args(arglist):
    """Parse command-line arguments.
    
    Expect two mandatory arguments:
        - computer_player: computer
        - names: one or more names of human players
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("names", nargs="*", help="player names")
    parser.add_argument("-c", "--computer_player", action="store_true",
                        help="add a computer player")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.names, args.computer_player)
    
    
#Test the code in terminal with this example (if mac): python3 filename player_name -c