from cgi import test
import random
from collections import defaultdict

class Deck():
    def __init__(self):
        self.card_types = ("ace", "two", "three", "four", "five", "six", "seven", 
              "eight", "nine", "ten", "jack", "queen", "king")
        self.suites = ("hearts", "diamonds", "spades", "clubs")

        # each card in the deck is represented as a tuple:
        # (card type, suite)
        self.deck = []
        for card_type in self.card_types:
            for suite in self.suites:
                self.deck.append((card_type, suite))

        # useful for checking card existence
        # dict of format {card value: num in deck}
        self.num_cards = {}
        for card_type in self.card_types:
            self.num_cards[card_type] = 4

        self.total_cards = len(self.deck)

    # checks if a card value is in the deck
    # returns true or false
    def card_value_in_deck(self, card_value):
        return self.num_cards[card_value] > 0
    
    def card_value_not_in_deck(self, card_value):
        return self.num_cards[card_value] == 0

    # draws a random card from deck
    # returns the drawn card or None if deck is empty
    def draw_card(self):
        if self.total_cards == 0:
            return None
        
        card = random.choice(self.deck)
        self.total_cards -= 1
        return card

    # resets deck to init state
    def reset_deck(self):
        self.__init__()
        return 

    # print() for the Deck class
    def __str__(self):
        total_cards_string = f'total cards: {self.total_cards}'
        num_cards_string = f'cards in deck: {self.num_cards}'

        return total_cards_string + '\n' + num_cards_string

        



if __name__ == "__main__":
    print("\n----------TESTING DECK INITIALIZATION----------")
    test_deck = Deck()
    print(test_deck)

    print("\n----------TESTING CARD EXISTENCE CHECK----------")
    for card_value in test_deck.card_types:
        if test_deck.card_value_in_deck(card_value):
            print(f'{card_value} in deck')
        else:
            print(f'{card_value} not in deck')
    
    print("\n----------TESTING CARD DRAWING----------")
    for i in range(10):
        drawn_card = test_deck.draw_card()
        print(f'drew card {drawn_card}: {test_deck.total_cards} cards left')

    print("\n----------TESTING DECK RESET----------")
    test_deck.reset_deck()
    print(test_deck)