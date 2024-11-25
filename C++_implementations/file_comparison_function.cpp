#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iterator>

std::vector<std::string> readListFromFile(const std::string& filename) {
    std::ifstream file(filename);
    std::vector<std::string> list;
    std::string line;

    while (getline(file, line)) {
        list.push_back(line);
    }

    std::sort(list.begin(), list.end());
    return list;
}

void writeDifferencesToFile(const std::vector<std::string>& list1, const std::vector<std::string>& list2, const std::string& filename) {
    std::ofstream file(filename);
    std::vector<std::string> diff;

    std::set_difference(list1.begin(), list1.end(), list2.begin(), list2.end(), std::back_inserter(diff));
    for (const auto& item : diff) {
        file << item << '\n';
    }
}

int main() {
    auto list1 = readListFromFile("list1.txt");
    auto list2 = readListFromFile("list2.txt");
    writeDifferencesToFile(list1, list2, "differences.csv");
    std::cout << "See the differences.csv for results in current directory" << std::endl;

    return 0;
}
