from products.api.models import Product

def get_products():
    products = [
        Product(id=1, name="Product 1", price=10.99),
        Product(id=2, name="Product 2", price=19.99),
        Product(id=3, name="Product 3", price=5.99),
    ]
    return products
