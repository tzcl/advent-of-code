#include <algorithm>
#include <array>
#include <fmt/core.h>
#include <fmt/format.h>
#include <fmt/ranges.h>
#include <iostream>
#include <numeric>
#include <sstream>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

struct point {
  int x = 0, y = 0;

  auto operator+=(const point &rhs) -> point & {
    this->x += rhs.x;
    this->y += rhs.y;
    return *this;
  }

  auto operator==(const point &rhs) const -> bool {
    return x == rhs.x && y == rhs.y;
  }

  auto clamp(int l, int r) -> point & {
    if (x < l)
      x = l;
    if (x > r)
      x = r;
    if (y < l)
      y = l;
    if (y > r)
      y = r;
    return *this;
  }

  struct hash {
    auto operator()(const point &p) const -> size_t {
      return std::hash<int>()(p.x) ^ std::hash<int>()(p.y);
    }
  };
};

auto operator+(const point &lhs, const point &rhs) -> point {
  return {lhs.x + rhs.x, lhs.y + rhs.y};
}

auto operator-(const point &lhs, const point &rhs) -> point {
  return {lhs.x - rhs.x, lhs.y - rhs.y};
}

template <> struct fmt::formatter<point> : fmt::formatter<std::pair<int, int>> {
  template <typename FormatContext>
  auto format(const point &p, FormatContext &ctx) const {
    return fmt::formatter<std::pair<int, int>>::format(std::make_pair(p.x, p.y),
                                                       ctx);
  }
};

auto dist(const point &a, const point &b) -> int {
  return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
}

auto adjacent(const point &a, const point &b) -> bool {
  point delta = a - b;
  return abs(delta.x) <= 1 && abs(delta.y) <= 1;
}

auto sgn(int x) -> int {
  if (x < 0) return -1;
  else if (x > 0) return 1;
  else return 0;
}

auto move_tail(const point &head, const point &tail) -> point {
  point diff = {head.x - tail.x, head.y - tail.y};
  if (abs(diff.x) <= 1 && abs(diff.y) <= 1)
    return {0, 0};
  return diff.clamp(-1, 1);
}

std::unordered_map<char, point> const dirs = {
    {'R', {1, 0}}, {'U', {0, 1}}, {'L', {-1, 0}}, {'D', {0, -1}}};

using move = std::pair<point, int>;

void grid(const std::unordered_set<point, point::hash> &points) {
  for (int row = 8; row >= -5; --row) {
    for (int col = -14; col < 14; ++col) {
      if (points.count({col, row}))
        fmt::print("#");
      else
        fmt::print(".");
    }
    fmt::print("\n");
  }
}

void part1(const std::vector<move> &moves) {
  std::unordered_set<point, point::hash> points;
  points.emplace(0, 0);

  point head{}, tail{}, prev{};
  for (const auto &[dir, steps] : moves) {
    for (int i = 0; i < steps; ++i) {
      prev = head;
      head += dir;
      if (dist(head, tail) > 2) {
        tail = prev;
        points.insert(tail);
      }
    }
  }

  fmt::print("positions: {}\n", size(points));
  grid(points);
}

void part2(const std::vector<move> &moves) {
  std::unordered_set<point, point::hash> head;
  std::unordered_set<point, point::hash> points;
  std::vector<point> rope(10, {0, 0});
  
  for (const auto &[dir, steps]: moves) {
    for (int i = 0; i < steps; ++i) {
      rope[0] += dir;
      
      for (int j = 1; j < size(rope); ++j) {
        if (!adjacent(rope[j-1], rope[j])) {
          point delta = rope[j-1] - rope[j];
          rope[j] = rope[j] + point{sgn(delta.x), sgn(delta.y)};
        }
      }
      
      points.insert(rope.back());
    }
  }
  
  fmt::print("size: {}\n", size(points));
  grid(points);
}

void solve(std::istream &input) {
  std::vector<move> moves;
  std::string line;
  while (getline(input, line)) {
    std::stringstream ss(line);
    char dir;
    int steps;
    ss >> dir >> steps;
    moves.emplace_back(dirs.at(dir), steps);
  }

  part1(moves);
  part2(moves);
}

int main() {
  solve(std::cin);

  return 0;
}
