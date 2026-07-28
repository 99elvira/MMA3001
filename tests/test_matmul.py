"""Test suite for the matmul() matrix multiplication function.

Implements both **positive tests** (valid inputs that should produce
correct results) and **negative tests** (invalid or edge‑case inputs
that should raise appropriate errors).

Test categories:
    - Positive: square matrices, identity, zero matrix, rectangular,
      single-element, random validation against NumPy.
    - Negative: incompatible dimensions, empty matrices, non-numeric
      inputs, ragged rows, None inputs.
"""

import pytest


# ── Module under test ────────────────────────────────────────────────
# Duplicated here so the test file is self-contained (the function
# lives in the Colab notebook / docs folder, not a pip‑installable
# package).  In a real project this would be an ``import``.
def matmul(A, B):
    """Multiply matrix A (m×n) by matrix B (n×p) → matrix C (m×p).

    Args:
        A: Left matrix as list of lists (m rows × n columns).
        B: Right matrix as list of lists (n rows × p columns).

    Returns:
        Result matrix C (m rows × p columns) as list of lists.

    Raises:
        ValueError: If either matrix is empty, has ragged rows, or
            inner dimensions do not match for multiplication.
    """
    # ── Input validation ────────────────────────────────────────────
    if not isinstance(A, list) or not isinstance(B, list):
        raise TypeError("Both A and B must be lists of lists.")
    if not A or not A[0] or not B or not B[0]:
        raise ValueError(
            "Matrices must be non-empty with at least one row and one column."
        )

    m, n = len(A), len(A[0])
    p = len(B[0])

    # Check B has correct number of rows
    if len(B) != n:
        raise ValueError(
            f"Inner dimensions must match: A is {m}×{n}, "
            f"but B has {len(B)} rows (expected {n})."
        )

    # Check for ragged rows in A
    for i, row in enumerate(A):
        if len(row) != n:
            raise ValueError(
                f"Row {i} of A has {len(row)} columns, expected {n}."
            )

    # Check for ragged rows in B
    for j, row in enumerate(B):
        if len(row) != p:
            raise ValueError(
                f"Row {j} of B has {len(row)} columns, expected {p}."
            )

    # ── Multiplication ──────────────────────────────────────────────
    C = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            s = 0
            for k in range(n):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C


# ══════════════════════════════════════════════════════════════════════
# POSITIVE TEST CASES — valid inputs, expected behaviour
# ══════════════════════════════════════════════════════════════════════

class TestMatmulPositive:
    """Tests that verify correct output for well‑formed inputs."""

    def test_square_2x2_matrices(self):
        """Multiply two 2×2 matrices and check every element."""
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        assert matmul(A, B) == expected

    def test_square_3x3_matrices(self):
        """Multiply two 3×3 matrices — validates the full triple‑loop."""
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        expected = [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
        assert matmul(A, B) == expected

    def test_identity_matrix(self):
        """Multiplying by the identity should return the original matrix."""
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        assert matmul(A, I) == A

    def test_zero_matrix(self):
        """Any matrix × zero matrix → zero matrix."""
        A = [[1, 2], [3, 4]]
        Z = [[0, 0], [0, 0]]
        assert matmul(A, Z) == [[0, 0], [0, 0]]

    def test_rectangular_m_times_n_by_n_times_p(self):
        """2×3 × 3×2 → 2×2 result."""
        A = [[1, 2, 3], [4, 5, 6]]  # 2×3
        B = [[7, 8], [9, 10], [11, 12]]  # 3×2
        expected = [[58, 64], [139, 154]]
        assert matmul(A, B) == expected

    def test_single_element_matrices(self):
        """1×1 × 1×1 should give the scalar product."""
        assert matmul([[3]], [[7]]) == [[21]]

    def test_row_vector_times_column_vector(self):
        """1×3 × 3×1 → 1×1 (dot product)."""
        A = [[1, 2, 3]]  # 1×3
        B = [[4], [5], [6]]  # 3×1
        assert matmul(A, B) == [[32]]  # 1*4 + 2*5 + 3*6

    def test_column_vector_times_row_vector(self):
        """3×1 × 1×3 → 3×3."""
        A = [[1], [2], [3]]  # 3×1
        B = [[4, 5, 6]]  # 1×3
        expected = [[4, 5, 6], [8, 10, 12], [12, 15, 18]]
        assert matmul(A, B) == expected

    def test_against_numpy(self):
        """Spot‑check against NumPy for a randomish 4×4 case."""
        import numpy as np
        A_list = [[1, 0, 2, 3], [4, 1, 0, 2], [3, 2, 1, 0], [0, 1, 2, 3]]
        B_list = [[2, 1, 0, 3], [1, 0, 3, 2], [0, 3, 2, 1], [3, 2, 1, 0]]
        expected = np.dot(np.array(A_list), np.array(B_list)).tolist()
        assert matmul(A_list, B_list) == expected

    def test_negative_numbers(self):
        """Handle matrices with negative entries correctly."""
        A = [[-1, 2], [3, -4]]
        B = [[5, -6], [-7, 8]]
        expected = [[-19, 22], [43, -50]]
        assert matmul(A, B) == expected

    def test_float_values(self):
        """Handle floating‑point entries."""
        A = [[0.5, 1.5], [2.5, 3.5]]
        B = [[4.0, 2.0], [1.0, 3.0]]
        expected = [[3.5, 5.5], [13.5, 15.5]]
        assert matmul(A, B) == expected


# ══════════════════════════════════════════════════════════════════════
# NEGATIVE TEST CASES — invalid inputs, should raise errors cleanly
# ══════════════════════════════════════════════════════════════════════

class TestMatmulNegative:
    """Tests that verify the function fails gracefully on bad input."""

    def test_incompatible_dimensions(self):
        """A 2×3 × 2×2 is invalid — inner dims must match."""
        A = [[1, 2, 3], [4, 5, 6]]  # 2×3
        B = [[7, 8], [9, 10]]  # 2×2 (should be 3×something)
        with pytest.raises(ValueError, match="Inner dimensions must match"):
            matmul(A, B)

    def test_empty_matrix_A(self):
        """An empty outer list cannot be multiplied."""
        A = []
        B = [[1, 2], [3, 4]]
        with pytest.raises(ValueError, match="non-empty"):
            matmul(A, B)

    def test_empty_inner_list(self):
        """A matrix with an empty row has no columns."""
        A = [[]]
        B = [[1]]
        with pytest.raises(ValueError, match="non-empty"):
            matmul(A, B)

    def test_empty_matrix_B(self):
        """An empty B matrix has no columns to index."""
        A = [[1, 2], [3, 4]]
        B = []
        with pytest.raises(ValueError, match="non-empty"):
            matmul(A, B)

    def test_ragged_rows_A(self):
        """Rows of different lengths in A should not be silently accepted."""
        A = [[1, 2, 3], [4, 5]]  # row 1 has 3 cols, row 2 has 2
        B = [[1, 2], [3, 4], [5, 6]]
        with pytest.raises(ValueError, match="Row 1 of A"):
            matmul(A, B)

    def test_ragged_rows_B(self):
        """Rows of different lengths in B should not be silently accepted."""
        A = [[1, 2, 3], [4, 5, 6]]  # 2×3
        B = [[1, 2], [3, 4], [5]]  # 3 rows but row 2 has only 1 col
        with pytest.raises(ValueError, match="Row 2 of B"):
            matmul(A, B)

    def test_none_input(self):
        """Passing None should fail immediately."""
        with pytest.raises(TypeError):
            matmul(None, [[1, 2], [3, 4]])

    def test_non_list_input(self):
        """Passing a string instead of a matrix should fail."""
        with pytest.raises(TypeError):
            matmul("not_a_matrix", [[1, 2], [3, 4]])
