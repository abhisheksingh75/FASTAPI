from fastapi import FastAPI, Response, Request
from typing import List, Dict
import json
from fastapi import HTTPException

tags_metadata = [
    {
        "name": "cart operations",
        "description": "Operations to manage an e-commerce cart using cookies."
    }
]

app = FastAPI(openapi_tags=tags_metadata)

# A simple representation of a product
class Product:
    def __init__(self, id: str, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price}

# Sample product inventory
product_inventory = {
    "p1": Product("p1", "Laptop", 999.99),
    "p2": Product("p2", "Smartphone", 499.99),
    "p3": Product("p3", "Headphones", 89.99)
}



@app.post("/add_to_cart")
def add_to_cart(response: Response, product_id: str, request: Request):
    product = product_inventory.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found in inventory")
    cart = json.loads(request.cookies.get("cart", "[]"))
    cart.append(product.to_dict())
    response.set_cookie(key="cart", value=json.dumps(cart))
    return {"message": f"Added {product.name} to cart."}


@app.get("/view_cart")
def view_cart(request: Request):
    cart = json.loads(request.cookies.get("cart", "[]"))
    return {"cart": cart}

@app.delete("/clear_cart")
def clear_cart(response: Response):
    response.delete_cookie(key="cart")
    return {"message": "Cart cleared"}

