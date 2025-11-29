from typing import Optional
import pytest
from common.list_node import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = current = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            carry, digit = divmod(
                carry + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10
            )
            current.next = ListNode(digit)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


# Tests
@pytest.mark.parametrize(
    "l1, l2, expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ],
)
def test_solution(l1, l2, expected):
    sol = Solution()
    l1_node = ListNode.from_list(l1)
    l2_node = ListNode.from_list(l2)
    result = sol.addTwoNumbers(l1_node, l2_node)
    assert result.to_list() == expected
