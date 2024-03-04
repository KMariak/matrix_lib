from typing import List
from asgiref.sync import sync_to_async
from .utils import get_matrix_string, convert_string_to_list, counter_clockwise_traversal
from .models import Matrix
from django.db import transaction


def add_string_matrix(matrix_string):
    with transaction.atomic():
        Matrix.objects.create(matrix=matrix_string)


async def get_matrix(url: str) -> List[int]:
    matrix_string = await get_matrix_string(url)
    matrix_list = convert_string_to_list(matrix_string)
    return counter_clockwise_traversal(matrix_list)


async def save_matrix(url):
    matrix_string = await get_matrix_string(url)
    await sync_to_async(add_string_matrix)(matrix_string)
    return 'Matrix was added'
