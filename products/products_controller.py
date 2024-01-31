# products/controllers/products_controller.py

from config.database import SessionLocal
from products.models import Product

def get_products():
    # Create a database session
    db = SessionLocal()

    try:
        # Fetch all products
        products = db.query(Product).all()
        return products
    except Exception as e:
        print(f"Error fetching products: {e}")
        return None
    finally:
        # Close session
        db.close()
