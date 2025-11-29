from typing import List
import pytest


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float("inf")
        n = len(nums)

        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum

        return closest_sum


# Tests
@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
    ],
)
def test_solution(nums, target, expected):
    sol = Solution()
    result = sol.threeSumClosest(nums, target)
    assert result == expected
