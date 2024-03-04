from typing import List


def validate_matrix(integer_values: List[int], matrix_size: int):
    if not integer_values:
        raise ValueError("No integer numbers found in the matrix string")

    if matrix_size ** 2 != len(integer_values):
        raise ValueError("Matrix is not square")

    if any(num < 0 for num in integer_values):
        raise ValueError("Negative numbers are not allowed")