#include <fstream>
#include <iostream>
#include <map>
#include <vector>
int main() {
	std::vector<std::string> inputData;
	
	std::fstream file("day8.txt");
    if (file.is_open()) {
        std::string line;
        while (getline(file, line)) {
            inputData.push_back(line);
        }
    }
    file.close();
	// inputData.clear();
	// inputData = {"LR",
    //          "",
    //          "AAA = (BBB, XXX)",
    //          "BBB = (XXX, ZZZ)",
    //          "ZZZ = (BBB, XXX)",
    //          "BBA = (AAB, XXX)",
    //          "AAB = (AAC, AAC)",
    //          "AAC = (AAZ, AAZ)",
    //          "AAZ = (AAB, AAB)",
    //          "XXX = (XXX, XXX)"
	// };
    
	std::map<std::string, std::map<char, std::string>> tree;
	for (std::string line : inputData) {
		if (line.find("=") != std::string::npos) {
			std::string head, left, right;
			head = line.substr(0, 3);
			left = line.substr(7, 3);
			right = line.substr(12, 3);

			std::map<char, std::string> children;
			children['L'] = left;
			children['R'] = right;

			tree[head] = children;
		}

	}
	std::string commands = inputData[0];

	std::vector<std::string> elements;
	for (auto const& [key, val] : tree) {
		if (key[2] == 'A') {
			elements.push_back(key);
		}
	}

    bool stopCond = false;
	int steps = 0;
	std::vector<std::vector<int>> history;
	history.resize(elements.size());
	for (int i = 0; i < 100000; i++) {
		int currStep = steps % commands.size();
		stopCond = true;
		std::vector<std::string> newElements;
		for (int j = 0; j < elements.size(); j++) {
			std::string element = elements[j];
			element = tree[element][commands[currStep]];
			newElements.push_back(element);
			if (element[2] == 'Z') {
				history[j].push_back(steps);
			}
		}
		steps += 1;
		elements = newElements;
	}
	for (int i = 0; i < history.size(); i++) {
		std::cout << elements[i] << ": \n";
		for (int j = 0; j < history[i].size(); j++) {
			std::cout << history[i][j] << std::endl;
		}
	}

}