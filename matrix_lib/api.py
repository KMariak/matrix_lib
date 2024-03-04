from ninja import NinjaAPI
from matrix_traversal.views import get_matrix, save_matrix

api = NinjaAPI()


@api.get("/get_square_matrix")
async def get_square_matrix(request, url):
    return await get_matrix(url)


@api.get("/save_square_matrix")
async def save_square_matrix(request, url):
    return await save_matrix(url)