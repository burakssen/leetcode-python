import pytest


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        index = 0
        if s[0] in ("+", "-"):
            if s[0] == "-":
                sign = -1
            index += 1

        result = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            result = result * 10 + digit
            index += 1

        result *= sign

        # Clamp the result to the 32-bit signed integer range
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result


# Tests
@pytest.mark.parametrize(
    "x, expected",
    [
        ("42", 42),
        (" -42", -42),
        ("1337c0d3", 1337),
        ("0-1", 0),
        ("words and 987", 0),
    ],
)
def test_solution(x, expected):
    sol = Solution()
    result = sol.myAtoi(x)
    assert result == expected
