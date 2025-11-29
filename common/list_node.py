from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"

    @staticmethod
    def from_list(values: List[int]) -> Optional['ListNode']:
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def to_list(self) -> List[int]:
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.to_list() == other.to_list()
