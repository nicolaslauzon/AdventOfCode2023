from utils.aoc_utils import AOCDay, day


@day(3)
class Day3(AOCDay):
    def common(self):
        return 0

    def part1(self):
        total = 0
        # self.inputData = [
        #     "467..114..",
        #     "...*......",
        #     "..35..633.",
        #     "......#...",
        #     "617*......",
        #     ".....+.58.",
        #     "..592.....",
        #     "......755.",
        #     "...$.*....",
        #     ".664.598..",
        # ]

        numberMatrix = self.buildPartNumberMatrix()

        for i in range(len(self.inputData)):
            for j in range(len(self.inputData[i])):
                partValues = set()
                if self.isSymbol(self.inputData[i][j]):
                    partValues = self.getPartValue(i, j, numberMatrix)
                for k in partValues:
                    total += k

        return total

    def part2(self):
        total = 0
        # self.inputData = [
        #     "467..114..",
        #     "...*......",
        #     "..35..633.",
        #     "......#...",
        #     "617*......",
        #     ".....+.58.",
        #     "..592.....",
        #     "......755.",
        #     "...$.*....",
        #     ".664.598..",
        # ]

        numberMatrix = self.buildPartNumberMatrix()

        for i in range(len(self.inputData)):
            for j in range(len(self.inputData[i])):
                partValues = set()
                if self.inputData[i][j] == "*":
                    partValues = self.getPartValue(i, j, numberMatrix)
                if 0 in partValues:
                    partValues.remove(0)
                if len(partValues) == 2:
                    partValues = list(partValues)
                    print(partValues)
                    total += partValues[0] * partValues[1]

        return total

    def buildPartNumberMatrix(self):
        partNumberMatrix = []
        for i in self.inputData:
            line = []
            currNumber = ""
            for idx, j in enumerate(i):
                if j >= "0" and j <= "9":
                    currNumber += j
                    if idx == len(i) - 1:
                        for _ in range(len(currNumber)):
                            line.append(int(currNumber))
                else:
                    if currNumber != "":
                        for _ in range(len(currNumber)):
                            line.append(int(currNumber))
                        currNumber = ""
                    line.append(0)

            partNumberMatrix.append(line)
        return partNumberMatrix

    def getPartValue(self, i, j, numberMatrix):
        lenght = len(self.inputData)
        partValues = set()
        if j > 0:
            partValues.add(numberMatrix[i][j - 1])

        if j < lenght - 1:
            partValues.add(numberMatrix[i][j + 1])

        if i > 0:
            partValues.add(numberMatrix[i - 1][j])
            if j > 0:
                partValues.add(numberMatrix[i - 1][j - 1])
            if j < lenght - 1:
                partValues.add(numberMatrix[i - 1][j + 1])

        if i < lenght - 1:
            partValues.add(numberMatrix[i + 1][j])
            if j > 0:
                partValues.add(numberMatrix[i + 1][j - 1])
            if j < lenght - 1:
                partValues.add(numberMatrix[i + 1][j + 1])
        return partValues

    #     total = 0
    #     for i in range(len(self.inputData)):
    #         top, middle, bottom = self.getRows(i)

    #         number = ""
    #         lastSymbolIdx = 0

    #         for j in range(len(middle)):
    #             isAdj = False
    #             currChar = middle[j]

    #             if top != "" and self.containsSymbol(top[lastSymbolIdx : j + 1]):
    #                 isAdj = True
    #             if bottom != "" and self.containsSymbol(bottom[lastSymbolIdx : j + 1]):
    #                 isAdj = True
    #             if self.isSymbol(middle[lastSymbolIdx]) or self.isSymbol(middle[j]):
    #                 isAdj = True

    #             if currChar >= "0" and currChar <= "9":
    #                 number += currChar
    #                 if j == len(middle) - 1:
    #                     total += int(number)
    #             else:
    #                 if number != "" and isAdj:
    #                     total += int(number)
    #                 lastSymbolIdx = j
    #                 number = ""

    #     return total

    # def containsSymbol(self, segment: str):
    #     for i in segment:
    #         if self.isSymbol(i):
    #             return True
    #     return False

    def isSymbol(self, c: chr):
        return c not in [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # def getRows(self, i):
    #     top = ""
    #     middle = ""
    #     bottom = ""

    #     middle = self.inputData[i]

    #     if i != 0:
    #         top = self.inputData[i - 1]

    #     if len(self.inputData) > i + 1:
    #         bottom = self.inputData[i + 1]

    #     return top, middle, bottom
