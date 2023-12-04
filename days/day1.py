from utils.aoc_utils import AOCDay, day

@day(1)
class Day1(AOCDay):
    def common(self):
        return None

    def part1(self):
        total = 0
        once = True
        for i in self.inputData:
            for j in i:
                if j >= '0' and j <= '9':
                    if once:
                        first = j
                        once = False
                    last = j
            once = True
            total += int(first + last)
        return total

    
    def part2(self):
        total = 0

#         input = [
# 'two1nine',
# 'eightwothree',
# 'abcone2threexyz',
# 'xtwone3four',
# '4nineeightseven2',
# 'zoneight234',
# '7pqrstsixteen',
#         ]
        # numbersTxt = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

        # for line in self.inputData:
        #     for i in range(len(line)):
        #         for number in numbersTxt:
        #             if number in line[0:i]:
        #                 line = line.replace(number, str(numbersTxt.index(number)+1), 1)


        #     numbers = []
        #     for i, letter in enumerate(line):
        #         if letter >= '0' and letter <= '9':
        #             numbers.append(letter)

        #     total += int(numbers[0] + numbers[-1])
        # return total

        total = 0
        for line in self.inputData:
            numbers = []
            for i, letter in enumerate(line):
                if letter.isdigit():
                    numbers.append(letter)

                for j, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                    if line[i:].startswith(val):
                        numbers.append(str(j+1))
            
            total += int(numbers[0] + numbers[-1])
        return total





    # iterate trough word
    # if letter try to match a number
    # if number do other thing