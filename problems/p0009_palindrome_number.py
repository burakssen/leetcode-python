import pytest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original = str(x)
        reversed_str = original[::-1]
        return original == reversed_str


# Tests
@pytest.mark.parametrize(
    "x, expected",
    [
        (121, True),
        (-121, False),
        (10, False),
    ],
)
def test_solution(x, expected):
    sol = Solution()
    result = sol.isPalindrome(x)
    assert result == expected
