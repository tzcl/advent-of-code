#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>

int count(const std::vector<int> &nums) {
  int count = 0;
  for (int i = 1; i < nums.size(); ++i) {
    if (nums[i] > nums[i - 1])
      ++count;
  }

  return count;
}

int count2(std::vector<int> nums) {
  std::adjacent_difference(std::begin(nums), std::end(nums), std::begin(nums));
  return std::ranges::count_if(nums, [](int i) { return i > 0;}) - 1;
}

int sum(int i, const std::vector<int> &nums) {
  // i >= 2
  return std::accumulate(std::cbegin(nums) + i, std::cbegin(nums) + i + 3, 0);
}

int window(const std::vector<int> &nums) {
  int count = 0, prev = sum(0, nums);
  for (int i = 1; i + 3 <= nums.size(); ++i) {
    int curr = sum(i, nums);
    if (curr > prev)
      ++count;
    prev = curr;
  }

  return count;
}

int main() {
  std::vector<int> nums;
  int num;
  while (std::cin >> num) {
    nums.push_back(num);
  }

  std::cout << count2(nums) << "\n";
  std::cout << window(nums) << "\n";

  return 0;
}
