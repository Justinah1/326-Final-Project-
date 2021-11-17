import random

""" This python script would be used to implement the experimental 
skeleton code of some of our methods that we've decided on for the final project"""


def highscore(file_path):
    """This method is used to keep track of the highscores 
    of the top 10 players in the game
    
    Args:
    file_path (str): this is the path to the text file needed to run the program
    """
    UserName = str(input("Enter a UserName: "))
    s = int(input("Enter new score: "))
    l =[UserName,s]
    with open(file_path, "r", encoding="utf-8") as f:
        f = f.readlines()
        score = []
        for line in f:
            line = line.strip()
            score.append(line.split(" "))
    
    score.sort(key=lambda x:int(x[1]), reverse = True)
    lowest_score = int(score[-1][1])
    highest_score = int(score[0][1])
    if s <= lowest_score:
        if len(score)>=10:
            score.pop()
        score.insert(-1, l)
    elif s >= highest_score:
        if len(score) >= 10:
            score.pop()
        score.insert(0, l)
    elif s > lowest_score and s < highest_score:
        if len(score)>= 10:
            score.pop()
        score.append(l)
        
    score.sort(key=lambda x:int(x[1]), reverse = True)
    print(score)

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        


def CompTurn(hand, currCard):

    goodHand = ()
    hasCard = False
    lowRank = 15
    highRank = 0
    deal = Card()
    
    if currCard.suit == "Spade":
        for card in hand:
            if card.suit == "Spade":
                goodHand.append(card)
                hasCard = True
            else: 
                goodHand = hand
    elif currCard.suit == "Club":
        for card in hand:
            if card.suit == "Club":
                goodHand.append(card)
                hasCard = True
            else: 
                goodHand = hand
    elif currCard.suit == "Heart":
        for card in hand:
            if card.suit == "Heart":
                goodHand.append(card)
                hasCard = True
            else: 
                goodHand = hand
    elif currCard.suit == "Diamond":
        for card in hand:
            if card.suit == "Diamond":
                goodHand.append(card)
                hasCard = True
            else: 
                goodHand = hand
    else:
        goodHand = hand

    if hasCard == True:
        for card in goodHand:
            if card.rank > highRank:
                deal = card
    elif hasCard == False:
        for card in goodHand:
            if card.rank < lowRank:
                deal = card
    
    return deal

def deal():
    """
    This method takes the list returned from the deck() function, shuffles it,
    and deals out 5 cards per round.
    
    Side effects:
    shuffles a deck (list) of card objects and then players' cardlist is updated
    with the cards they obtain by popping them out from the shuffled card deck.
    """
    deck = deck() 
    shuffledDeck = deck.shuffle()
        
    for player in playersList:
        amountOfCardsPerTrick = 1
        while amountOfCardsPerTrick <= 5:
            player.cards.append(shuffledDeck.pop)
            amountOfCardsPerTrick += 1    
    
def deck(self):
    """This method creates and sets the deck of cards 

    Returns:
        deck [str]: returns all deck card values
    """
    
    face = ["K","Q","J","A", "6", "7", "8", "9", "10"]
    suits = ["Hearts","Spades","Clubs","Diamonds"]
    deck = []
    for i in face:
        for x in suits:
            deck.append(x + " of " + i)
    return deck    