#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

struct Round {
  std::string l;
  std::string r;
};

const std::unordered_map<std::string, int> shape{
    {"A", 0}, {"B", 1}, {"C", 2}, {"X", 0}, {"Y", 1}, {"Z", 2},
};

const std::unordered_map<std::string, int> outcome{
    {"W", 6}, {"D", 3}, {"L", 0}, {"X", 0}, {"Y", 3}, {"Z", 6},
};

const std::unordered_map<int, std::string> choice{{0, "A"}, {1, "B"}, {2, "C"}};

std::string play1(Round r) {
  if ((shape.at(r.l) + 1) % 3 == shape.at(r.r))
    return "W";
  else if (shape.at(r.l) == shape.at(r.r))
    return "D";
  else
    return "L";
}

std::string play2(Round r) {
  if (r.r == "X") {
    return choice.at(((shape.at(r.l) - 1) % 3 + 3) % 3);
  } else if (r.r == "Y") {
    return choice.at(shape.at(r.l));
  } else {
    return choice.at((shape.at(r.l) + 1) % 3);
  }
}

int main() {
  std::vector<Round> rounds;
  for (std::string line; std::getline(std::cin, line);) {
    std::stringstream ss(line);
    Round r;
    ss >> r.l >> r.r;
    rounds.emplace_back(r);
  }

  int sum1 = 0, sum2 = 0;
  for (auto r : rounds) {
    sum1 += shape.at(r.r) + 1 + outcome.at(play1(r));
    sum2 += shape.at(play2(r)) + 1 + outcome.at(r.r);
  }

  std::cout << sum1 << "\n";
  std::cout << sum2 << "\n";

  return 0;
}
