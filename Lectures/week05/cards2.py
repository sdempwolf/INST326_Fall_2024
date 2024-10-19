import random  # we will use this module to shuffle the cards

class cards():

    # a deck of cards has four suits with 13 cards (ranks) in each suit.
    # the cards may have different values depending on the game. for now, we'll use these.
    # in some card games, one suit may 'trump' another suit, meaning it has a higher value. we'll skip for now.
    
    
    # when we call a class to construct an object, the __init__ method runs automatically.
    # this method initializes some of the object's variables and sets their starting values.
    
    def __init__(self, suits, ranks, card_values):
        self.suits = suits
        self.ranks = ranks
        self.card_values = card_values
        self.newcard = {}
        self.deck = []
      
    # we define a method to create a deck of cards. although self.deck is initialized above, we do so again
    # in the method to ensure that it creates a new deck of 52 cards every time.
    
    def make_deck(self):
        self.deck = [] 
        for suit in self.suits: # loop through the suits
            for index, rank in enumerate(self.ranks): # loop through the ranks; enumerate gives us the index number
                value = self.card_values[index] # We use the index number here to get the card value
                newcard = {'suit':suit, 'rank':rank, 'value':value} #create a new card dictionary
                self.deck.append(newcard) # append the new card to the deck list

    # both the make_deck method and shuffle method act on the self.deck attribute.
    # that is, they change the elements and order of the object's deck list inside the object.
    # they do not return anything explicitly, yet we end up with a shuffled deck.
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        card = self.deck.pop()
        return card

    # when we deal a physical card, we take the top card off the deck and put it in the player's hand.
    # the dealt card is no longer available in the deck.
    # the list.pop() method accomplishes this. just think of the end of the list as the top of the deck.
    # as cards are dealt, the number of remaining cards in the deck decreases.

    def print_name(self):
        print('name = ', __name__)

# the following code lets you test the code above if this code is run independently.
# but it doesn't run when this code is run as a module.

if __name__ == "__main__":
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    gamedeck = cards(suits, ranks, card_values)
    gamedeck.make_deck()
    gamedeck.shuffle()
    print(gamedeck.deck)
    print(len(gamedeck.deck))
