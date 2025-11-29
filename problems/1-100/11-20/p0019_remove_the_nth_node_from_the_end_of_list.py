from typing import Optional
from common.list_node import ListNode
import pytest


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next

        # Remove the nth node from end
        second.next = second.next.next

        return dummy.next


# Tests
@pytest.mark.parametrize(
    "head, n, expected",
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
    ],
)
def test_solution(head, n, expected):
    sol = Solution()
    head_node = ListNode.from_list(head)
    result_node = sol.removeNthFromEnd(head_node, n)
    result = ListNode.to_list(result_node)
    assert result == expected
