from typing import Optional
import pytest
from common.list_node import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next


# Tests
@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ],
)
def test_solution(list1, list2, expected):
    sol = Solution()
    list1 = ListNode.from_list(list1)
    list2 = ListNode.from_list(list2)
    result = sol.mergeTwoLists(list1, list2)
    result = ListNode.to_list(result)
    assert result == expected
