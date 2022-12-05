#include <algorithm>
#include <deque>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Move {
  int src, dst, n;
};

enum class State { STACKS, MOVES };

void print(vector<char> const &v) {
  for (auto const &c : v) {
    cout << c << " ";
  }
  cout << "\n";
}

void print(deque<char> const &v) {
  for (auto const &c : v) {
    cout << c << " ";
  }
  cout << "\n";
}

void part1(Move m, vector<deque<char>> &stacks) {
  for (int k = 0; k < m.n; ++k) {
    stacks[m.dst].push_back(stacks[m.src].back());
    stacks[m.src].pop_back();
  }
}

void part2(Move m, vector<deque<char>> &stacks) {
  copy_n(end(stacks[m.src]) - m.n, m.n, back_inserter(stacks[m.dst]));
  for (int k = 0; k < m.n; ++k)
    stacks[m.src].pop_back();
}

int main() {
  vector<deque<char>> stacks(10);
  vector<Move> moves;

  State state = State::STACKS;
  string line;
  while (getline(cin, line)) {
    switch (state) {
    case State::STACKS:
      if (line.empty()) {
        state = State::MOVES;
        break;
      }

      for (int i = 0; i < size(line); ++i) {
        if (line[i] == ' ' || line[i] == '[' || line[i] == ']')
          continue;
        int index = (i - 1) / 4;
        stacks[index].push_front(line[i]);
      }
      break;
    case State::MOVES:
      int i, j, n;
      sscanf(line.c_str(), "move %d from %d to %d", &n, &i, &j);
      moves.emplace_back(i - 1, j - 1, n);
      break;
    }
  }

  for (const auto &m : moves) {
    part1(m, stacks);
    // part2(m, stacks);
  }

  for (auto &s : stacks) {
    if (!s.empty())
      cout << s.back();
    else
      cout << ".";
  }
  cout << "\n";

  return 0;
}
