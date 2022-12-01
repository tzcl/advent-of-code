#include <algorithm>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>

int max(std::vector<int> &elves) {
  return *std::max_element(std::begin(elves), std::end(elves));
}

int top_three(std::vector<int> &elves) {
  std::sort(std::rbegin(elves), std::rend(elves));
  return std::accumulate(std::begin(elves), std::begin(elves) + 3, 0);
}

int main() {
  std::vector<int> elves;
  int sum{};
  // How can I make this logic nicer?
  for (std::string line; std::getline(std::cin, line); ) {
    try {
      const int num{std::stoi(line)};
      sum += num;
    } catch (std::invalid_argument const &ex) {
      elves.push_back(sum);
      sum = 0;
    }
  }
  // Final sum doesn't get appended
  elves.push_back(sum);
    
  std::cout << max(elves) << "\n";
  std::cout << top_three(elves) << "\n";

  return 0;
}
