from utils.aoc_utils import AOCDay, day


@day(5)
class Day5(AOCDay):
    def common(self):
        self.inputData = [
            "seeds: 79 14 55 13",
            "",
            "seed-to-soil map:",
            "50 98 2",
            "52 50 48",
            "",
            "soil-to-fertilizer map:",
            "0 15 37",
            "37 52 2",
            "39 0 15",
            "",
            "fertilizer-to-water map:",
            "49 53 8",
            "0 11 42",
            "42 0 7",
            "57 7 4",
            "",
            "water-to-light map:",
            "88 18 7",
            "18 25 70",
            "",
            "light-to-temperature map:",
            "45 77 23",
            "81 45 19",
            "68 64 13",
            "",
            "temperature-to-humidity map:",
            "0 69 1",
            "1 0 69",
            "",
            "humidity-to-location map:",
            "60 56 37",
            "56 93 4",
        ]
        self.inputData.append("")

    def part1(self):
        maps = self.generateMaps()

        seeds = self.inputData[0].split(": ")[1].split(" ")
        locations = []
        for seed in seeds:
            seed = int(seed)
            for map in maps:
                tmpSeed = None
                for i in range(len(map["destination"])):
                    destination = map["destination"][i]
                    source = map["source"][i]
                    rangeLen = map["rangeLen"][i]
                    if seed >= source and seed <= source + rangeLen:
                        tmpSeed = seed - source + destination
                        break
                if tmpSeed != None:
                    seed = tmpSeed
            locations.append(seed)
        return min(locations)

    def part2(self):
        maps = self.generateMaps()

        seedsStr = self.inputData[0].split(": ")[1].split(" ")

        seeds = []
        for i in range(0, len(seedsStr), 2):
            seed = {
                "start": int(seedsStr[i]),
                "length": int(seedsStr[i + 1]) - 1,
            }
            seeds.append(seed)

        for map in maps:
            newSeeds = []
            while len(seeds) > 0:
                seed = seeds.pop()
                newSeeds += self.getNextSeeds(seed, map)
            seeds = newSeeds

        return min(seeds)

    def getNextSeeds(self, inSeed, map):
        newSeeds = []

        seedsToCheck = [inSeed]

        for i in range(len(map["destination"])):
            for seed in seedsToCheck:
                print(seed)
                destination = map["destination"][i]
                mapLeft = map["source"][i]
                mapRange = map["rangeLen"][i]
                seedLeft = seed["start"]
                seedRange = seed["length"]

                if seedLeft >= mapLeft and seedLeft + seedRange <= mapLeft + mapRange:
                    seedsToCheck.remove(seed)
                    newSeeds.append(
                        {
                            "start": seedLeft - mapLeft + destination,
                            "length": seedRange,
                        }
                    )
                    break
                elif seedLeft < mapLeft and seedLeft + seedRange > mapLeft + mapRange:
                    seedsToCheck.remove(seed)
                    newSeeds.append(
                        {
                            "start": destination,
                            "length": mapRange,
                        }
                    )
                    seedsToCheck.append(
                        {"start": seedLeft, "length": mapLeft - seedLeft - 1}
                    )
                    seedsToCheck.append(
                        {
                            "start": mapLeft + mapRange + 1,
                            "length": seedLeft + seedRange - mapLeft - mapRange - 1,
                        }
                    )
                    break
                elif seedLeft < mapLeft:
                    seedsToCheck.remove(seed)
                    newSeeds.append(
                        {
                            "start": destination,
                            "length": seedLeft + seedRange - mapLeft,
                        }
                    )
                    seedsToCheck.append(
                        {"start": seedLeft, "length": mapLeft - seedLeft - 1}
                    )
                    break
                elif seedLeft + seedRange > mapLeft + mapRange:
                    seedsToCheck.remove(seed)
                    newSeeds.append(
                        {
                            "start": seedLeft - mapLeft + destination,
                            "length": mapRange - seedLeft + mapLeft,
                        }
                    )
                    seedsToCheck.append(
                        {
                            "start": mapLeft + mapRange + 1,
                            "length": seedLeft + seedRange - mapLeft - mapRange - 1,
                        }
                    )
                    break
        return newSeeds + seedsToCheck

    def generateMaps(self):
        maps = []
        for i in range(len(self.inputData)):
            if "map" in self.inputData[i]:
                i += 1
                data = []
                while self.inputData[i] != "":
                    data += [self.inputData[i].split(" ")]
                    i += 1
                map = self.createMap(data)
                maps.append(map)
        return maps

    def createMap(self, data):
        map = {}
        map["destination"] = []
        map["source"] = []
        map["rangeLen"] = []
        for line in data:
            map["destination"] += [int(line[0])]
            map["source"] += [int(line[1])]
            map["rangeLen"] += [int(line[2]) - 1]
        return map
