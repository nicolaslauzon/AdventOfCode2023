#include <iostream>
#include <fstream>
#include <vector>
#include <thread>
#include <algorithm>
#include <mutex>

static std::vector<long> locations;

struct Map {
    std::vector<long> destination;
    std::vector<long> source;
    std::vector<long> rangeLen;
};

struct Seed {
    long seed;
    long range;
};

Map createMap(std::vector<std::vector<std::string>> data) {
    Map map;
    for (auto line : data) {
        map.destination.push_back(std::stol(line[0]));
        map.source.push_back(std::stol(line[1]));
        map.rangeLen.push_back(std::stol(line[2]) - 1);
    }
    return map;
}

std::vector<Map> generateMaps(std::vector<std::string> inputData) {
    std::vector<Map> maps;

    for (int i = 0; i < inputData.size(); i++) {
        if (inputData[i].find("map") != std::string::npos) {
            i++;
            std::vector<std::vector<std::string>> data;
            while (inputData[i] != "") {
                if (i == inputData.size()) break;
                std::string line = inputData[i];
                std::string number = "";
                std::vector<std::string> lineData;
                for (auto c : line) {
                    if (c >= '0' && c <= '9') {
                        number += c;
                    } else {
                        lineData.push_back(number);
                        number = "";
                    }
                }
                lineData.push_back(number);
                data.push_back(lineData);
                i++;
            }
            Map map = createMap(data);
            maps.push_back(map);
        }
    }
    return maps;
}

std::vector<Seed> parseSeeds(std::string seedString) {
    std::vector<long> seedNums;
    std::string number = "";
    for (char c : seedString) {
        if (c >= '0' && c <= '9') {
            number += c;
        } else {
            seedNums.push_back(std::stol(number));
            number = "";
        }
    }
    seedNums.push_back(std::stol(number));
    
    std::vector<Seed> seeds;
    for (int i = 0; i < seedNums.size(); i += 2) {
        Seed seed;
        seed.seed = seedNums[i];
        seed.range = seedNums[i + 1];
        seeds.push_back(seed);
    }
    return seeds;
}

void computeSeedResult(const Seed& seed, const std::vector<Map>& maps, long& location) {
    long smallestSeed = __LONG_MAX__;
    for (long seedValue = seed.seed; seedValue < seed.seed + seed.range; seedValue++) {
        long seedRes = seedValue;
        for (const Map& map : maps) {
            long tmpSeed = -1;
            for (int i = 0; i < map.destination.size(); i++) {
                long dest = map.destination[i];
                long src = map.source[i];
                long rangeLen = map.rangeLen[i];
                if (seedRes >= src && seedRes <= src + rangeLen) {
                    tmpSeed = seedRes - src + dest;
                    break;
                }
            }
            if (tmpSeed != -1) {
                seedRes = tmpSeed;
            }
        }
        if (smallestSeed > seedRes) {
            smallestSeed = seedRes;
            std::cout << smallestSeed << std::endl;
        }
    }
}

int main() {
    std::ifstream file("day5.txt");
    std::vector<std::string> inputData;
    int threadCount = 0;
    if (file.is_open()) {
        std::string line;
        while (getline(file, line)) {
            inputData.push_back(line);
        }
    }
    file.close();

    std::vector<Map> maps = generateMaps(inputData);
    std::vector<Seed> seeds = parseSeeds(inputData[0].substr(inputData[0].find(": ") + 2));
    std::vector<std::thread> threads;
    for (const Seed& seed : seeds) {
        long location = 0;
        locations.push_back(location);
        threads.push_back(std::thread(computeSeedResult, std::ref(seed), std::ref(maps), std::ref(location)));
            threadCount++;
    }
    for (auto& thread : threads) {
        thread.join();
    }
    std::cout << *std::min_element(locations.begin(), locations.end()) << std::endl;
}