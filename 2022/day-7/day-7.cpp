#include <fstream>
#include <functional>
#include <iostream>
#include <memory>
#include <sstream>
#include <unordered_map>
#include <vector>

using namespace std;

class node {
  // A raw pointer is appropriate here, because we know that the parent will
  // outlive the child, and needs to be nullptr. The reason we don't use
  // shared_ptr or weak_ptr is that the child never *owns* the parent.
  //
  // An alternative would be to use a reference (through std::reference_wrapper)
  // but that requires knowing the object at construction and can't be nullptr.
public:
  node *parent;
  unordered_map<string, unique_ptr<node>> children;
  int size{0};

  node(node *parent_) : parent(parent_) {}
};

class input_buffer {
public:
  input_buffer(ifstream &input) {
    string line;
    while (getline(input, line)) {
      buffer.push_back(line);
    }
  }

  auto next_line() -> string { return buffer[pos++]; }

  auto done() -> bool { return pos >= size(buffer); }

  auto peek_cmd() -> bool { return done() || buffer[pos][0] == '$'; }

private:
  vector<string> buffer;
  int pos{0};
};

auto split(const string &s) -> vector<string> {
  istringstream iss(s);
  vector<string> tokens;
  string token;
  while (iss >> token) {
    tokens.push_back(token);
  }

  return tokens;
}

auto split_file(const string &s) -> pair<string, string> {
  istringstream iss(s);
  vector<string> tokens;
  string token;
  while (iss >> token) {
    tokens.push_back(token);
  }

  return {tokens[0], tokens[1]};
}

auto propagate_size(node &n) -> int {
  if (n.children.empty()) {
    return n.size;
  }

  for (const auto &[_, c] : n.children) {
    n.size += propagate_size(*c);
  }

  return n.size;
}

void traverse(node &n, const function<void(node &)> func) {
  func(n);

  if (n.children.empty()) {
    return;
  }

  for (const auto &[_, c] : n.children) {
    traverse(*c, func);
  }
}

auto part1(node &tree) -> int {
  int acc{};
  auto filter = [&acc](node &n) mutable {
    if (n.size <= 100'000) {
      acc += n.size;
    }
  };
  traverse(tree, filter);

  return acc;
}

auto part2(node &tree) -> int {
  int need = 30'000'000 - (70'000'000 - tree.size);
  
  int acc = numeric_limits<int>::max();
  auto visit = [&acc, need](node &n) mutable {
    if (n.size >= need) {
      acc = min(acc, n.size);
    }
  };
  traverse(tree, visit);
  
  return acc;
}

void solve(ifstream &input) {
  input_buffer buf(input);

  // Parse input into the tree
  auto tree = make_unique<node>(nullptr);
  node *curr = tree.get();

  while (!buf.done()) {
    auto line = buf.next_line();
    auto tokens = split(line);
    auto cmd = tokens[1];

    if (cmd == "cd") {
      auto path = tokens[2];
      if (path == "/")
        continue;
      else if (path == "..") {
        curr = curr->parent;
      } else
        curr = curr->children[path].get();
    } else {
      while (!buf.peek_cmd()) {
        auto line = buf.next_line();
        auto [token, path] = split_file(line);

        if (token == "dir") {
          curr->children[path] = make_unique<node>(curr);
        } else {
          int size = stoi(token);
          curr->size += size;
        }
      }
    }
  }

  cout << "Total size: " << propagate_size(*tree) << "\n";

  cout << part1(*tree) << "\n";
  cout << part2(*tree) << "\n";
}

int main() {
  cout << "Sample\n";
  ifstream sample("sample");
  solve(sample);

  cout << "Input\n";
  ifstream input("input");
  solve(input);

  return 0;
}