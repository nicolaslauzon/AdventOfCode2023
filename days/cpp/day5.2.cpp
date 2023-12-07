
    // def part1(self):
    //     maps = self.generateMaps()

    //     seeds = self.inputData[0].split(": ")[1].split(" ")
    //     locations = []
    //     for seed in seeds:
    //         seed = int(seed)
    //         for map in maps:
    //             tmpSeed = None
    //             for i in range(len(map["destination"])):
    //                 destination = map["destination"][i]
    //                 source = map["source"][i]
    //                 rangeLen = map["rangeLen"][i]
    //                 if seed >= source and seed <= source + rangeLen:
    //                     tmpSeed = seed - source + destination
    //                     break
    //             if tmpSeed != None:
    //                 seed = tmpSeed
    //         locations.append(seed)
    //     return min(locations)

    // def generateMaps(self):
    //     maps = []
    //     for i in range(len(self.inputData)):
    //         if "map" in self.inputData[i]:
    //             i += 1
    //             data = []
    //             while self.inputData[i] != "":
    //                 data += [self.inputData[i].split(" ")]
    //                 i += 1
    //             map = self.createMap(data)
    //             maps.append(map)
    //     return maps

#include <iostream>

int main() {
    std::cout << "Hello World!\n";
}