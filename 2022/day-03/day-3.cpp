#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int priority(char c) {
  int res = c - 'a' + 1;
  if (res <= 0) res += 58;
  return res;
}

int part1(vector<pair<string, string>> &rucksacks) {
  int sum = 0;

  for (const auto &r : rucksacks) {
    string shared;
    ranges::set_intersection(r.first, r.second, back_inserter(shared));

    for (const auto &c : shared) {
      sum += priority(c);
    }
  }
  
  return sum;
}

int main() {
  vector<pair<string, string>> rucksacks;
  string rucksack;
  while (cin >> rucksack) {
    int len = size(rucksack) / 2;
    string first = rucksack.substr(0, len);
    string second = rucksack.substr(len, size(rucksack));

    ranges::sort(first);
    first.erase(unique(begin(first), end(first)), end(first));
    ranges::sort(second);
    second.erase(unique(begin(second), end(second)), end(second));
    rucksacks.emplace_back(first, second);
  }

  cout << part1(rucksacks) << "\n";
  
  return 0;
}
