#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int priority(char c) {
  int res = c - 'a' + 1;
  if (res <= 0) res += 58;
  return res;
}

int main() {
	vector<string> rucksacks;
	string line;
	while (cin >> line) {
		// Sort and dedup
		ranges::sort(line);
		line.erase(unique(begin(line), end(line)), end(line));
		rucksacks.push_back(line);
	}
	
	// Compute groups
	vector<char> groups;
	for (int i = 0; i < size(rucksacks); i += 3) {
		string tmp, group;
		ranges::set_intersection(rucksacks[i], rucksacks[i+1], back_inserter(tmp));
		ranges::set_intersection(tmp, rucksacks[i+2], back_inserter(group));
		// Should only contain one character
		groups.push_back(group[0]);
 	}
	
	int sum = 0;
	for (auto c : groups) {
		sum += priority(c);
	}
	cout << sum << "\n";
}