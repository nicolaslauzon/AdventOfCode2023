import re
from utils.aoc_utils import AOCDay, day


@day(8)
class Day8(AOCDay):
    def common(self):
        # print(self.inputData)
        return 0

    def part1(self):
        # self.inputData = [
        #     "LLR",
        #     "",
        #     "AAA = (BBB, BBB)",
        #     "BBB = (AAA, ZZZ)",
        #     "ZZZ = (ZZZ, ZZZ)",
        # ]
        tree = {}
        for i in self.inputData:
            if "=" in i:
                head, left, right = re.findall(r"[A-Z]+", i)
                tree[head] = {"L": left, "R": right}
        commands = self.inputData[0]

        element = "AAA"
        last = "ZZZ"

        steps = 0
        while element != last:
            currStep = steps % len(commands)
            element = tree[element][commands[currStep]]
            steps += 1

        return steps

    def part2(self):
        # self.inputData = [
        #     "LR",
        #     "",
        #     "AAA = (BBB, XXX)",
        #     "BBB = (XXX, ZZZ)",
        #     "ZZZ = (BBB, XXX)",
        #     "BBA = (AAB, XXX)",
        #     "AAB = (AAC, AAC)",
        #     "AAC = (AAZ, AAZ)",
        #     "AAZ = (AAB, AAB)",
        #     "XXX = (XXX, XXX)",
        # ]
        tree = {}
        for i in self.inputData:
            if "=" in i:
                head, left, right = re.findall(r"[A-Z]+", i)
                tree[head] = {"L": left, "R": right}
        commands = self.inputData[0]

        elements = list(filter(lambda x: x[-1] == "A", tree.keys()))
        print(elements)
        stopCond = False

        steps = 0
        while stopCond is False:
            currStep = steps % len(commands)
            stopCond = True
            newElements = []
            for element in elements:
                element = tree[element][commands[currStep]]
                newElements.append(element)
                if element[-1] != "Z":
                    stopCond = False
            steps += 1
            elements = newElements

        return steps
