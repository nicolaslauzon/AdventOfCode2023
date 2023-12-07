from utils.aoc_utils import AOCDay, day
import re


@day(6)
class Day6(AOCDay):
    def common(self):
        # print(self.inputData)
        return 0
        # timeHeld * (length - timeHeld)

    def part1(self):
        # self.inputData = [
        #     "Time:      7  15   30",
        #     "Distance:  9  40  200",
        # ]
        _, timeStr = self.inputData[0].split(":")
        times = list(map(int, re.findall(r"\d+", timeStr)))

        _, distanceStr = self.inputData[1].split(":")
        distances = list(map(int, re.findall(r"\d+", distanceStr)))

        total = 1
        for i in range(len(times)):
            raceTotal = 0
            for timeHeld in range(times[i]):
                raceDistance = timeHeld * (times[i] - timeHeld)
                if raceDistance > distances[i]:
                    raceTotal += 1
            total *= raceTotal
        return total

    def part2(self):
        # self.inputData = [
        #     "Time:      7  15   30",
        #     "Distance:  9  40  200",
        # ]
        _, timeStr = self.inputData[0].split(":")
        times = re.findall(r"\d+", timeStr)
        time = ""
        for i in times:
            time += i
        time = int(time)

        _, distanceStr = self.inputData[1].split(":")
        distances = re.findall(r"\d+", distanceStr)
        distance = ""
        for i in distances:
            distance += i
        distance = int(distance)

        raceTotal = 0
        for timeHeld in range(time):
            raceDistance = timeHeld * (time - timeHeld)
            if raceDistance > distance:
                raceTotal += 1
        return raceTotal
