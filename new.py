import sys
import os
import re
from datetime import date

TEMPLATE = """from typing import List, Optional
import pytest
# from common.list_node import ListNode
# from common.tree_node import TreeNode

class Solution:
    def solve(self):
        pass

# Tests
@pytest.mark.parametrize("input_args, expected", [
    # Example 1
    (
        (),
        None
    ),
])
def test_solution(input_args, expected):
    sol = Solution()
    assert sol.solve(*input_args) == expected
"""

def sanitize_filename(name):
    # Lowercase and replace spaces/non-alphanumerics with underscores
    s = name.lower()
    s = re.sub(r'[^a-z0-9]+', '_', s)
    return s.strip('_')

def main():
    if len(sys.argv) < 2:
        print("Usage: python new.py <problem_name_or_url>")
        sys.exit(1)

    raw_name = " ".join(sys.argv[1:])
    filename = sanitize_filename(raw_name)
    
    # If it starts with a number, ensure it's padded or handled nicely, 
    # but simple sanitization is usually enough. 
    # Users often paste "1. Two Sum", so let's handle that specific pattern.
    match = re.match(r'^(\d+)_+(.*)', filename)
    if match:
        num = int(match.group(1))
        rest = match.group(2)
        filename = f"p{num:04d}_{rest}"
    
    filepath = os.path.join("problems", f"{filename}.py")

    if os.path.exists(filepath):
        print(f"Error: File {filepath} already exists.")
        sys.exit(1)

    with open(filepath, "w") as f:
        f.write(TEMPLATE)

    print(f"Created {filepath}")

if __name__ == "__main__":
    main()
