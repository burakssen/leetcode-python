import pytest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        start = max_length = 0

        for i, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1
            char_index_map[char] = i
            max_length = max(max_length, i - start + 1)

        return max_length


# Tests
@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ],
)
def test_solution(s, expected):
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    assert result == expected
