import unittest
import deck_cards 


class DeckCardsTable(unittest.TestCase):
    def setUp(self):
        self.deck = deck_cards.Deck()

    def test_deck(self):
        deck = deck_cards.Deck()
        self.assertEqual(len(deck.cards), 52)
        cards = [1] * 52
        expect = [0] * 52
        for i in range(52):
            expect[deck.cards[i]] = 1
        self.assertEqual(cards, expect)

    def test_card(self):
        pk = deck_cards.PokerCard(5, deck_cards.Suit(2))
        self.assertEqual(pk.value, 5)
        self.assertEqual(pk.suit, deck_cards.Suit(2))

    def test_hand(self):
        hand = deck_cards.Hand()
        self.assertLess(len(hand.all_cards()), 5)
        for i in range(5):
            card = i
            hand.add_card(card)

        self.assertEqual(hand.ranking(), deck_cards.Rank.STRAIGHT_FLUSH)
        hand2 = deck_cards.Hand()
        hand2.add_card(0)
        hand2.add_card(13)
        hand2.add_card(26)
        hand2.add_card(39)
        self.assertEqual(hand2.ranking(), deck_cards.Rank.FOLD)
        hand2.add_card(1)
        self.assertEqual(hand2.ranking(), deck_cards.Rank.FOUR_OF_A_KIND)

        hand3 = deck_cards.Hand()
        hand3.add_card(10)
        hand3.add_card(12)
        hand3.add_card(8)
        hand3.add_card(11)
        hand3.add_card(9)
        self.assertEqual(hand3.ranking(), deck_cards.Rank.ROYAR_FLUSH)

        hand4 = deck_cards.Hand()
        hand4.add_card(10)
        hand4.add_card(12)
        hand4.add_card(13)
        hand4.add_card(11)
        hand4.add_card(9)
        self.assertEqual(hand4.ranking(), deck_cards.Rank.HIGH_CARD)


        
if __name__ == '__main__':
    unittest.main()
