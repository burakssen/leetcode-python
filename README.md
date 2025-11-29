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
