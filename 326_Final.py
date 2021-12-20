from argparse import ArgumentParser
import sys
import random
<<<<<<< HEAD

=======
>>>>>>> ed24b3764efb913d59a055461fdfff4c6826170c
    
class Spar:
    
    def __init__(self, score, deck = [], playersList = [], currCard = None):
        self.score = score
        self.deck = deck
        self.playersList = playersList
        self.currCard = currCard
        
    
    def newDeck(self):
        """This method creates and sets the deck of cards 
        Returns:
        deck [str]: returns all deck card values
    """
    
        face = [14, 13, 12, 11, 10, 9, 8, 7, 6]
        suits = ["Hearts","Spades","Clubs","Diamonds"]
        deck = []
        for i in face:
            for x in suits:
                if x != "Spades" and i != 14:
                    deck.append(Card(i, x))
        return deck 
        
    def deal(self):
        shuffledDeck = self.newDeck()
        random.shuffle(shuffledDeck)
        
        for player in self.playersList:
            amountOfCardsPerTrick = 1
            while amountOfCardsPerTrick <= 5:
                player.dealCards(shuffledDeck.pop())
                amountOfCardsPerTrick += 1  
                
    def setCurrCard(self, player):
        self.currCard = player.playTurn()
        
    def scoring(self, num):
        if num == 6:
            return 3
        elif num == 7:
            return 2
        else:
            return 1
            
    def game(self): 
        compScore = 0
        round = 0
        trick = 0
        
        self.deal()
        
        compTrick = False
        
        while round < 5:
        
            if trick == 0:
                self.setCurrCard(self.playersList[0])
                compCardPlayed = self.playersList[1].compTurn()
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
    def __init__(self, face, suit):
        self.suit = suit
        self.face = face
    
    def __repr__(self):
        return (f"Card({self.suit},{self.face}")    
        
   # def __str__(self):
   #     print("test")
        
         
            
class Player:
    def __init__(self, name, currCard = Card(14, "Hearts"), cards = []):
        self.name = name
        self.cards = cards
        self.currCard = currCard
        
    def dealCards(self, card):
        self.cards.append(card)
        
    #def __str__(self):
    #    print("test")
        
    def playTurn(self):
       
        for card in self.cards:
            print(card)
        first_card = int(input("Select a card (Using a number)"))
        self.currCard = self.cards.pop(first_card - 1)
        return self.currCard
    
class ComputerPlayer:
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

def main(human_players, computer_player):
    players = [Player(human_players), ComputerPlayer(computer_player)]
   
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
