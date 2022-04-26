# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
player_score = 0
dealer_score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# Deck


#Hands


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object

    def __str__(self):
        # return a string representation of a hand
        ans = 'Hand contains '
        for card in self.hand:
            ans += str(card) + ' '            
        return ans
    
    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        self.hand_value = 0
        ace = False
        aces = ['CA','SA','HA','DA']
        
        for card in self.hand:
            self.hand_value += VALUES[card.get_rank()]
            if str(card) in aces:
                ace = True
        
        if ace:
            if self.hand_value + 10 <= 21:
                self.hand_value += 10
                           
        return self.hand_value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.hand:
            card.draw(canvas, pos)
            pos[0] += 80
 
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop(-1)
    
    def __str__(self):
        # return a string representing the deck
        ans = 'Deck contains '
        for card in self.deck:
            ans += str(card) + ' '
        return ans



#define event handlers for buttons
def deal():
    global outcome, in_play, deck, playerHand, dealerHand, message, dealer_score
    
    if in_play:
        outcome = 'Player lost because of re-deal!. New deal?'
        dealer_score += 1
        in_play = False
        
    else:
        deck = Deck()
        deck.shuffle()
        outcome = 'Welcome to a new Game!'
        
        # Create Hands
        playerHand = Hand()
        dealerHand = Hand()
        
        # Add 2 cards to each Hand
        playerHand.add_card(deck.deal_card())
        playerHand.add_card(deck.deal_card())
        dealerHand.add_card(deck.deal_card())
        dealerHand.add_card(deck.deal_card())
        
        message = 'Hit or Stand?'
    
        in_play = True

def hit():
    global in_play, outcome, message, player_score, dealer_score
    if in_play:
        if playerHand.get_value() <= 21:
            playerHand.add_card(deck.deal_card())
        
        if playerHand.get_value() > 21:
            outcome = 'You have busted. Nee deal?'
            in_play = False
            dealer_score += 1
            message = ''
 
       
def stand():
    global in_play, dealerHand, outcome, player_score, dealer_score, message
     
    if in_play:
        while dealerHand.get_value() < 17:
            dealerHand.add_card(deck.deal_card())

        if dealerHand.get_value() > 21:
            outcome = 'Dealer busted. Congratulations!'
            player_score += 1
            message = 'New Deal?'

        else:
            if dealerHand.get_value() >= playerHand.get_value() or playerHand.get_value() > 21:
                outcome = "Dealer wins. New deal?"
                dealer_score += 1
                message = ''
            else:
                outcome = "Player wins. New deal?"
                player_score += 1
                message = ''
                
        in_play = False

# draw handler    
def draw(canvas):
    global outcome, player_score, dealer_score, message
    
    canvas.draw_text("Blackjack", [220, 50], 50 ,"Lime")
    
    #Hands
    playerHand.draw(canvas, [100,300])
    dealerHand.draw(canvas, [100, 150])
    
    #Outcome/Messages
    canvas.draw_text(outcome, [10, 100], 30 ,"Lime")
    canvas.draw_text(message, [200,480], 26, "Black")
    
    #Scores
    canvas.draw_text("Dealer: %s" % dealer_score, [10, 150], 20 ,"Black")
    canvas.draw_text("Player: %s" % player_score, [10, 300], 20 ,"White")

    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (136,199), CARD_BACK_SIZE)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
# CodeSkulptor = https://py2.codeskulptor.org/#user49_miuPvh3RWy_7.py