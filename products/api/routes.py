from fastapi import APIRouter
from products.controllers.products_controller import get_products

router = APIRouter()

@router.get("/products")
async def get_all_products():
    return get_products()
