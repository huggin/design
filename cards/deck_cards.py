from abc import ABCMeta, abstractmethod
from enum import Enum
import random


class Suit(Enum):
    HEART = 0
    DIAMOND = 1
    CLUBS = 2
    SPADE = 3


class Card(metaclass=ABCMeta):
    def __init__(self, value, suit):
        self._value = value
        self._suit = suit

    @property
    @abstractmethod
    def value(self):
        pass

    @value.setter
    @abstractmethod
    def value(self, other):
        pass


class PokerCard(Card):
    def __init__(self, value, suit):
        super().__init__(value, suit)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, other):
        self._value = other

    @property
    def suit(self):
        return self._suit


class Rank(Enum):
    FOLD = -1
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAR_FLUSH = 9


class Hand(object):
    POKER_CARDS = 5

    def __init__(self) -> None:
        self.cards = []
        self.rank = Rank.FOLD

    def add_card(self, card):
        self.cards.append(card)

    def fold(self):
        self.rank = Rank.FOLD

    def all_cards(self):
        if len(self.cards) != self.POKER_CARDS:
            return []
        cards = []
        for i in range(self.POKER_CARDS):
            suit, value = divmod(self.cards[i], 13)
            cards.append(PokerCard(value, Suit(suit)))
        return cards

    def ranking(self):
        cards = self.all_cards()
        if len(cards) != self.POKER_CARDS:
            return Rank.FOLD
        
        cards.sort(key = lambda x : (x.value, x.suit.value), reverse=True)
        suits = set()
        values = [0 for _ in range(14)]
        for i in range(self.POKER_CARDS):
            suits.add(cards[i].suit)
            values[cards[i].value] += 1

        if len(suits) == 1:
            ans = Rank.FLUSH
            if cards[0].value == cards[4].value + 4:
                ans = Rank.STRAIGHT_FLUSH
                if cards[0].value == 12:
                    ans = Rank.ROYAR_FLUSH
            return ans
        
        two, three = 0, 0
        for i in range(0, 13):
            if values[i] == 4:
                return Rank.FOUR_OF_A_KIND
            elif values[i] == 3:
                three += 1
            elif values[i] == 2:
                two += 1

        if three == 1:
            if two == 1:
                return Rank.FULL_HOUSE
            return Rank.THREE_OF_A_KIND
        
        if two == 2:
            return Rank.TWO_PAIRS
        elif two == 1:
            return Rank.ONE_PAIR
        
        if cards[0].value == cards[4].value + 4:
            return Rank.STRAIGHT

        return Rank.HIGH_CARD
        

        
class Deck(object):
    NUMBER_SUITS = 4
    NUMBER_PER_SUIT = 13

    def __init__(self, cards=None, shuffle=True):
        if cards is None:
            self.cards = [c for c in range(52)]
            random.seed()
            if shuffle:
                self.shuffle()
        else:
            self.cards = cards
        self.curr = 0

    def remaining_cards(self):
        return len(self.cards) - self.curr

    def deal_card(self):
        card = self.cards[self.curr]
        self.curr += 1
        return card

    def shuffle(self):
        for i in range(52):
            j = random.randrange(i, 52)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
