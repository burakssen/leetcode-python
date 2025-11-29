import pytest


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_abs = abs(x)

        reversed_str = str(x_abs)[::-1]
        reversed_int = sign * int(reversed_str)

        # Check for 32-bit signed integer overflow
        if reversed_int < -(2**31) or reversed_int > 2**31 - 1:
            return 0

        return reversed_int


# Tests
@pytest.mark.parametrize(
    "x, expected",
    [
        (123, 321),
        (-123, -321),
        (120, 21),
    ],
)
def test_solution(x, expected):
    sol = Solution()
    result = sol.reverse(x)
    assert result == expected
