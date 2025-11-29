from typing import List
import pytest


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)
        return (merged[n // 2] + merged[~n // 2]) / 2


# Tests
@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
    ],
)
def test_solution(nums1, nums2, expected):
    sol = Solution()
    result = sol.findMedianSortedArrays(nums1, nums2)
    assert result == expected
