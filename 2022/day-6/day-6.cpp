#include <fmt/core.h>
#include <fstream>
#include <string>

using namespace std;

auto uniq(const string &line, int n) -> int {
  int window = 0;

  for (int i = 0; i < size(line); ++i) {
    window ^= 1 << (line[i] - 'a'); // initialise the array
    if (i >= n) {                   // check for dups
      window ^= 1 << (line[i - n] - 'a');
      if (__builtin_popcount(window) == n)
        return i + 1;
    }
  }

  return -1;
}

void solve(ifstream &input) {
  string line;
  while (input >> line) {
    fmt::print("{}\n", uniq(line, 4));
    fmt::print("{}\n", uniq(line, 14));
  }
}

int main() {
  fmt::print("Sample\n");
  ifstream sample("sample");
  solve(sample);

  fmt::print("Input\n");
  ifstream input("input");
  solve(input);

  return 0;
}
