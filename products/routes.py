from fastapi import APIRouter, HTTPException
from products.products_controller import get_products

router = APIRouter()

@router.get("/products")
async def get_all_products():
    products = get_products()
    if products:
        return {
            "status": "success",
            "code": 200,
            "message": "Products retrieved successfully",
            "result": products
        }
    else:
        raise HTTPException(status_code=404, detail="No products found")