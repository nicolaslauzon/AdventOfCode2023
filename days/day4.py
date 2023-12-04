from utils.aoc_utils import AOCDay, day


@day(4)
class Day4(AOCDay):
    def common(self):
        return 0

    def part1(self):
        # self.inputData = [
        #     "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        #     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        #     "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        #     "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        #     "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        #     "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        # ]
        total = 0
        for i in self.inputData:
            _, numbers = i.split(": ")
            winningNumberStr, ourNumberStr = numbers.split(" | ")
            winningNumbers = winningNumberStr.split(" ")
            ourNumbers = ourNumberStr.split(" ")
            winningNumbers = [i for i in winningNumbers if i != ""]
            ourNumbers = [i for i in ourNumbers if i != ""]

            firstMatch = True
            cardTotal = 0
            for n in ourNumbers:
                if n in winningNumbers:
                    if firstMatch:
                        cardTotal = 1
                        firstMatch = False
                    else:
                        cardTotal *= 2
            total += cardTotal
        return total

    def part2(self):
        # self.inputData = [
        #     "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        #     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        #     "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        #     "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        #     "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        #     "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        # ]
        cards = []
        for i in self.inputData:
            card, numbers = i.split(": ")
            cardNumber = int(card[4:])
            winningNumberStr, ourNumberStr = numbers.split(" | ")
            winningNumbers = winningNumberStr.split(" ")
            ourNumbers = ourNumberStr.split(" ")
            winningNumbers = [i for i in winningNumbers if i != ""]
            ourNumbers = [i for i in ourNumbers if i != ""]

            numMatch = 0
            for n in ourNumbers:
                if n in winningNumbers:
                    numMatch += 1

            cards.append(numMatch)

        cardsToScratch = []
        for i, m in enumerate(cards):
            cardsToScratch.append({"number": i + 1, "matches": m})

        total = 0
        print(cardsToScratch)
        print(cards)
        while len(cardsToScratch) > 0:
            total += 1
            card = cardsToScratch.pop()
            for i in range(card["matches"]):
                number = card["number"] + i + 1
                cardToAppend = {"number": number, "matches": cards[number - 1]}
                cardsToScratch.append(cardToAppend)

        return total
