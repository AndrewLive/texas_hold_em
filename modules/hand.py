from cgi import test
import deck_module

# check best possible hand:
# takes a deck object for an argument
# checks current cards in hand and deck and evaluates best
# possible hand

class Hand():
    def __init__(self):
        self.hand = []
        self.num_cards = 0
        return

    # draws random card from specified deck
    def draw_card(self, deck):
        self.hand.append(deck.draw_card())
        self.num_cards += 1
        return

    # print function for hand
    def __str__(self):
        num_cards_string = f'cards in hand: {self.num_cards}'
        hand_string = f'cards: {self.hand}'
        return num_cards_string + '\n' + hand_string + '\n'




if __name__ == "__main__":
    test_deck = deck_module.Deck()
    print(test_deck)

    test_hand = Hand()
    print(test_hand)

    print('\n----------TESTING DRAWING TO HAND----------')
    test_hand.draw_card(test_deck)
    print(test_deck)
    print(test_hand)