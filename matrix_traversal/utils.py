import httpx
import re
from django.http import HttpResponseServerError
from .validation import validate_matrix
from typing import List


async def get_matrix_string(url):
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.text
    except httpx.HTTPStatusError as exc:
        return HttpResponseServerError(f"HTTP status error: {exc}")
    except httpx.TimeoutException as exc:
        return HttpResponseServerError(f"Connection timeout error: {exc}")
    except httpx.RequestError as exc:
        return HttpResponseServerError(f"Request error: {exc}")
    except Exception as exc:
        return HttpResponseServerError(f"Unexpected error: {exc}")


def convert_string_to_list(matrix_string):
    integer_values = list(map(int, re.findall(r'\d+', matrix_string)))
    matrix_size = int(len(integer_values) ** 0.5)
    validate_matrix(integer_values, matrix_size)
    return [integer_values[i:i+matrix_size] for i in range(0, len(integer_values), matrix_size)]


def counter_clockwise_traversal(matrix: List[List[int]]) -> List[int]:
    rows = len(matrix)
    columns = len(matrix[0])
    top_row = 0
    left_column = 0
    count = 0
    total_elements = rows * columns
    result = []

    while top_row < rows and left_column < columns:
        if count == total_elements:
            break
        for i in range(top_row, rows):
            result.append(matrix[i][left_column])
            count += 1
        left_column += 1
        if count == total_elements:
            break
        for i in range(left_column, columns):
            result.append(matrix[rows - 1][i])
            count += 1
        rows -= 1
        if count == total_elements:
            break
        if top_row < rows:
            for i in range(rows - 1, top_row - 1, -1):
                result.append(matrix[i][columns - 1])
                count += 1
            columns -= 1
        if count == total_elements:
            break
        if left_column < columns:
            for i in range(columns - 1, left_column - 1, -1):
                result.append(matrix[top_row][i])
                count += 1
            top_row += 1

    return result
