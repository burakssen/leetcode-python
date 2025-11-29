# LeetCode Solutions in Python

This repository contains my solutions to various LeetCode problems, implemented in Python.

## Project Structure

- `problems/`: This directory contains the solutions to individual LeetCode problems. Each problem is typically stored in a file named `pXXXX_problem_name.py`, where `XXXX` is the problem ID and `problem_name` is a short description of the problem.
- `common/`: This directory contains common data structures or utility functions that are used across multiple LeetCode problems (e.g., `list_node.py` for linked lists, `tree_node.py` for binary trees).
- `conftest.py`: Configuration for `pytest`, ensuring that modules in `problems/` can correctly import utilities from `common/`.
- `pyproject.toml`: Project metadata and dependency management.

## Setup

This project uses `uv` for dependency management.

1.  **Install `uv` (if you haven't already):**

    ```bash
    pip install uv
    ```

    or

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2.  **Install dependencies:**
    ```bash
    uv pip install -e . --with dev
    ```

This project is configured to use Python 3.12. You can use `pyenv` or `conda` to manage Python versions.

## Running Tests

Tests are written using `pytest`. To run all tests:

```bash
pytest
```

To run tests for a specific problem (e.g., `p0001_two_sum.py`):

```bash
pytest problems/p0001_two_sum.py
```

## Solved Problems

| #    | Problem Name                                                                                                                                     | Difficulty                                            | Status                                                    |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- | --------------------------------------------------------- |
| 0001 | [Two Sum](https://leetcode.com/problems/two-sum)                                                                                                 | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Solved](https://img.shields.io/badge/Solved-00C851)     |
| 0002 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers)                                                                                 | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Solved](https://img.shields.io/badge/Solved-00C851)     |
| 0003 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)                   | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Solved](https://img.shields.io/badge/Solved-00C851)     |
| 0004 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays)                                                         | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Solved](https://img.shields.io/badge/Solved-00C851)     |
| 0005 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring)                                                     | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Solved](https://img.shields.io/badge/Solved-00C851)     |
| 0006 | [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion)                                                                             | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Solved](https://img.shields.io/badge/Solved-00C851)     |
| 0007 | [Reverse Integer](https://leetcode.com/problems/reverse-integer)                                                                                 | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Solved](https://img.shields.io/badge/Solved-00C851)     |
| 0008 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi)                                                                 | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Solved](https://img.shields.io/badge/Solved-00C851)     |
| 0009 | [Palindrome Number](https://leetcode.com/problems/palindrome-number)                                                                             | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Solved](https://img.shields.io/badge/Solved-00C851)     |
| 0010 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching)                                                         | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Solved](https://img.shields.io/badge/Solved-00C851)     |
| 0011 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water)                                                             | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Solved](https://img.shields.io/badge/Solved-00C851)     |
| 0012 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman)                                                                               | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Solved](https://img.shields.io/badge/Solved-00C851)     |
| 0013 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer)                                                                               | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Solved](https://img.shields.io/badge/Solved-00C851)     |
| 0014 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix)                                                                     | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Solved](https://img.shields.io/badge/Solved-00C851)     |
| 0015 | [3Sum](https://leetcode.com/problems/3sum)                                                                                                       | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0016 | [3Sum Closest](https://leetcode.com/problems/3sum-closest)                                                                                       | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0017 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number)                                     | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0018 | [4Sum](https://leetcode.com/problems/4sum)                                                                                                       | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0019 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list)                                               | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0020 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses)                                                                             | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0021 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists)                                                                   | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0022 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses)                                                                       | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0023 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists)                                                                       | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0024 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs)                                                                         | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0025 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group)                                                               | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0026 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array)                                         | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0027 | [Remove Element](https://leetcode.com/problems/remove-element)                                                                                   | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0028 | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string)           | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0029 | [Divide Two Integers](https://leetcode.com/problems/divide-two-integers)                                                                         | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0030 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words)                             | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0031 | [Next Permutation](https://leetcode.com/problems/next-permutation)                                                                               | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0032 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses)                                                             | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0033 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array)                                                   | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0034 | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array) | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0035 | [Search Insert Position](https://leetcode.com/problems/search-insert-position)                                                                   | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0036 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku)                                                                                       | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0037 | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver)                                                                                     | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0038 | [Count and Say](https://leetcode.com/problems/count-and-say)                                                                                     | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0039 | [Combination Sum](https://leetcode.com/problems/combination-sum)                                                                                 | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0040 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii)                                                                           | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0041 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive)                                                                   | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0042 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water)                                                                         | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0043 | [Multiply Strings](https://leetcode.com/problems/multiply-strings)                                                                               | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0044 | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching)                                                                             | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0045 | [Jump Game II](https://leetcode.com/problems/jump-game-ii)                                                                                       | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0046 | [Permutations](https://leetcode.com/problems/permutations)                                                                                       | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0047 | [Permutations II](https://leetcode.com/problems/permutations-ii)                                                                                 | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0048 | [Rotate Image](https://leetcode.com/problems/rotate-image)                                                                                       | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0049 | [Group Anagrams](https://leetcode.com/problems/group-anagrams)                                                                                   | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0050 | [Pow(x, n)](https://leetcode.com/problems/powx-n)                                                                                                | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0051 | [N-Queens](https://leetcode.com/problems/n-queens)                                                                                               | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0052 | [N-Queens II](https://leetcode.com/problems/n-queens-ii)                                                                                         | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0053 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray)                                                                               | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0054 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix)                                                                                     | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0055 | [Jump Game](https://leetcode.com/problems/jump-game)                                                                                             | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0056 | [Merge Intervals](https://leetcode.com/problems/merge-intervals)                                                                                 | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0057 | [Insert Interval](https://leetcode.com/problems/insert-interval)                                                                                 | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0058 | [Length of Last Word](https://leetcode.com/problems/length-of-last-word)                                                                         | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0059 | [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii)                                                                               | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0060 | [Permutation Sequence](https://leetcode.com/problems/permutation-sequence)                                                                       | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0061 | [Rotate List](https://leetcode.com/problems/rotate-list)                                                                                         | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0062 | [Unique Paths](https://leetcode.com/problems/unique-paths)                                                                                       | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0063 | [Unique Paths II](https://leetcode.com/problems/unique-paths-ii)                                                                                 | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0064 | [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum)                                                                               | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0065 | [Valid Number](https://leetcode.com/problems/valid-number)                                                                                       | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0066 | [Plus One](https://leetcode.com/problems/plus-one)                                                                                               | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0067 | [Add Binary](https://leetcode.com/problems/add-binary)                                                                                           | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0068 | [Text Justification](https://leetcode.com/problems/text-justification)                                                                           | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0069 | [Sqrt(x)](https://leetcode.com/problems/sqrtx)                                                                                                   | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0070 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs)                                                                                 | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0071 | [Simplify Path](https://leetcode.com/problems/simplify-path)                                                                                     | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0072 | [Edit Distance](https://leetcode.com/problems/edit-distance)                                                                                     | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0073 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes)                                                                             | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0074 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix)                                                                           | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0075 | [Sort Colors](https://leetcode.com/problems/sort-colors)                                                                                         | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0076 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring)                                                               | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0077 | [Combinations](https://leetcode.com/problems/combinations)                                                                                       | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0078 | [Subsets](https://leetcode.com/problems/subsets)                                                                                                 | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0079 | [Word Search](https://leetcode.com/problems/word-search)                                                                                         | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0080 | [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii)                                   | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0081 | [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii)                                             | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0082 | [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii)                                     | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0083 | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list)                                           | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0084 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram)                                                   | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0085 | [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle)                                                                             | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0086 | [Partition List](https://leetcode.com/problems/partition-list)                                                                                   | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0087 | [Scramble String](https://leetcode.com/problems/scramble-string)                                                                                 | ![Hard](https://img.shields.io/badge/Hard-FF0000)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0088 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array)                                                                           | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0089 | [Gray Code](https://leetcode.com/problems/gray-code)                                                                                             | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0090 | [Subsets II](https://leetcode.com/problems/subsets-ii)                                                                                           | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0091 | [Decode Ways](https://leetcode.com/problems/decode-ways)                                                                                         | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0092 | [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii)                                                                   | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0093 | [Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses)                                                                       | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0094 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal)                                                     | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0095 | [Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii)                                                     | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0096 | [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees)                                                           | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0097 | [Interleaving String](https://leetcode.com/problems/interleaving-string)                                                                         | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0098 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree)                                                         | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0099 | [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree)                                                           | ![Medium](https://img.shields.io/badge/Medium-FFA500) | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
| 0100 | [Same Tree](https://leetcode.com/problems/same-tree)                                                                                             | ![Easy](https://img.shields.io/badge/Easy-5CB85C)     | ![Unsolved](https://img.shields.io/badge/Unsolved-FF0000) |
