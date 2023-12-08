from utils.aoc_utils import AOCDay, day
from dataclasses import dataclass
from functools import cmp_to_key


@dataclass
class Hand:
    hand: str
    bid: int
    handScore: int = 0


def isFiveOfAKind(hand: str):
    return hand[0] == hand[1] == hand[2] == hand[3] == hand[4]


def isFourOfAKind(hand: str):
    for i in hand:
        if hand.count(i) == 4:
            return True
    return False


def isFullHouse(hand: str):
    return isThreeOfAKind(hand) and isPair(hand)


def isThreeOfAKind(hand: str):
    for i in hand:
        if hand.count(i) == 3:
            return True
    return False


def isTwoPairs(hand: str):
    pairs = 0
    iSeen = []
    for i in hand:
        if hand.count(i) == 2 and i not in iSeen:
            pairs += 1
            iSeen.append(i)
    return pairs == 2


def isPair(hand: str):
    for i in hand:
        if hand.count(i) == 2:
            return True
    return False


@day(7)
class Day7(AOCDay):
    def common(self):
        # print(self.inputData)
        return 0

    def part1(self):
        # self.inputData = [
        #     "32T3K 765",
        #     "T55J5 684",
        #     "KK677 28",
        #     "KTJJT 220",
        #     "QQQJA 483",
        # ]
        hands = []
        for i in self.inputData:
            hand, bid = i.split(" ")
            hands.append(Hand(hand, int(bid)))
        hands = self.sortHands(hands)
        total = 0
        for i, hand in enumerate(hands):
            total += hand.bid * (i + 1)
            print(hand.handScore)
        return total

    def part2(self):
        return 0

    def sortHands(self, hands):
        for hand in hands:
            if isFiveOfAKind(hand.hand):
                hand.handScore = 6
            elif isFourOfAKind(hand.hand):
                hand.handScore = 5
            elif isFullHouse(hand.hand):
                hand.handScore = 4
            elif isThreeOfAKind(hand.hand):
                hand.handScore = 3
            elif isTwoPairs(hand.hand):
                hand.handScore = 2
            elif isPair(hand.hand):
                hand.handScore = 1
            else:
                hand.handScore = 0
        return sorted(hands, key=cmp_to_key(self.compareHands))

    def compareHands(self, hand1, hand2):
        if hand1.handScore > hand2.handScore:
            return 1
        if hand1.handScore < hand2.handScore:
            return -1
        for i in range(5):
            if self.compareCards(hand1.hand[i], hand2.hand[i]) > 0:
                return 1
            if self.compareCards(hand1.hand[i], hand2.hand[i]) < 0:
                return -1

    def compareCards(self, card1, card2):
        cardsRank = "23456789TJQKA"
        return cardsRank.index(card1) - cardsRank.index(card2)
