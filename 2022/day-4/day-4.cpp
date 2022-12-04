#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

struct Range {
  int l;
  int r;
};

auto contains(Range a, Range b) -> bool {
  return (a.l <= b.l && b.r <= a.r) || (b.l <= a.l && a.r <= b.r);
}

auto overlaps(Range a, Range b) -> bool {
  return (a.l <= b.l && b.l <= a.r) || (b.l <= a.l && a.l <= b.r);
}

auto part1(vector<Range> &first, vector<Range> &second) -> int {
  int count = 0;
  for (int i = 0; i < size(first); ++i) {
    if (contains(first[i], second[i])) {
      ++count;
    }
  }

  return count;
}

auto part2(vector<Range> &first, vector<Range> &second) -> int {
  int count = 0;
  for (int i = 0; i < size(first); ++i) {
    if (overlaps(first[i], second[i])) {
      ++count;
    }
  }
  
  return count;
}

auto main() -> int {
  vector<Range> first;
  vector<Range> second;

  std::string line;
  while (getline(cin, line)) {
    int a, b, c, d;
    sscanf(line.c_str(), "%d-%d,%d-%d", &a, &b, &c, &d);
    first.emplace_back(a, b);
    second.emplace_back(c, d);
  }

  cout << part1(first, second) << "\n";
  cout << part2(first, second) << "\n";

  return 0;
}
