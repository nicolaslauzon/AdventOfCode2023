from utils.aoc_utils import AOCDay, day

@day(2)
class Day2(AOCDay):
    def common(self):
        return 0

    def part1(self):
        total = 0

        for i in self.inputData:
            id, game = i.split(": ")
            id = int(id.split(" ")[1])
            gameIsPossible = True
            
            for sets in game.split("; "):
                redQty = 12
                greenQty = 13
                blueQty = 14

                for action in sets.split(", "):
                    qty, color = action.split(" ")
                    
                    if color == "red":
                        redQty -= int(qty)
                    elif color == "green":
                        greenQty -= int(qty)
                    elif color == "blue":
                        blueQty -= int(qty)
                    
                if (redQty < 0 or greenQty < 0 or blueQty < 0):
                    gameIsPossible = False
                    break
            if (gameIsPossible):
                total += id
        
        return total



    
    def part2(self):
        total = 0

        for i in self.inputData:
            id, game = i.split(": ")
            id = int(id.split(" ")[1])

            minRed = 0
            minGreen = 0
            minBlue = 0
            
            for sets in game.split("; "):
                setMinRed = 0
                setMinGreen = 0
                setMinBlue = 0

                for action in sets.split(", "):
                    qty, color = action.split(" ")
                    
                    if color == "red":
                        setMinRed += int(qty)
                    elif color == "green":
                        setMinGreen += int(qty)
                    elif color == "blue":
                        setMinBlue += int(qty)
                    
                if (setMinRed > minRed):
                    minRed = setMinRed
                if (setMinGreen > minGreen):
                    minGreen = setMinGreen
                if (setMinBlue > minBlue):
                    minBlue = setMinBlue

            power = minRed * minGreen * minBlue
            total += power
        
        return total
