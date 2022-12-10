#include <fmt/core.h>
#include <fmt/ranges.h>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

constexpr array<pair<int, int>, 4> dirs = {{{-1, 0}, {0, -1}, {1, 0}, {0, 1}}};

auto valid(int row, int col, const vector<vector<int>> &grid) -> bool {
  int n = size(grid);
  return row >= 0 && col >= 0 && row < n && col < n;
}

auto is_visible(int row, int col, const vector<vector<int>> &grid) -> bool {
  for (const auto &dir : dirs) {
    for (int nc = col + dir.first, nr = row + dir.second;;
         nc += dir.first, nr += dir.second) {
      if (!valid(nr, nc, grid))
        return true;
      if (grid[nr][nc] >= grid[row][col])
        break;
    }
  }

  return false;
}

auto part1(const vector<vector<int>> &grid) -> int {
  int count{0};
  for (int row = 0; row < size(grid); ++row) {
    for (int col = 0; col < size(grid); ++col) {
      if (is_visible(row, col, grid)) {
        count++;
      }
    }
  }

  return count;
}

auto score(int row, int col, const vector<vector<int>> &grid) -> int {
  int acc{1};
  for (const auto &dir : dirs) {
    int dist{0};
    for (int nc = col + dir.first, nr = row + dir.second; valid(nr, nc, grid);
         nc += dir.first, nr += dir.second) {
      ++dist;
      if (grid[nr][nc] >= grid[row][col]) break;
    }
    acc *= dist;
  }

  return acc;
}

auto part2(const vector<vector<int>> &grid) -> int {
  int acc{0};
  for (int row = 0; row < size(grid); ++row) {
    for (int col = 0; col < size(grid); ++col) {
      acc = max(acc, score(row, col, grid));
    }
  }

  return acc;
}

void solve(ifstream &input) {
  vector<vector<int>> grid;

  string line;
  while (getline(input, line)) {
    vector<int> row(size(line));
    for (int i = 0; i < size(line); ++i) {
      row[i] = line[i] - '0';
    }
    grid.push_back(row);
  }

  fmt::print("count: {}\n", part1(grid));
  fmt::print("score: {}\n", part2(grid));
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
