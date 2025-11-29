from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

    @staticmethod
    def from_list(values: List[Optional[int]]) -> Optional['TreeNode']:
        """Creates a binary tree from a list using LeetCode's level-order format."""
        if not values:
            return None
        
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1
        while queue and i < len(values):
            node = queue.popleft()
            
            # Left child
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
            # Right child
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        return root

    def to_list(self) -> List[Optional[int]]:
        """Converts the tree back to a list in LeetCode's level-order format."""
        if not self:
            return []
        
        result = []
        queue = deque([self])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        
        # Trim trailing Nones
        while result and result[-1] is None:
            result.pop()
            
        return result
    
    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return False
        return self.to_list() == other.to_list()
