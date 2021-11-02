from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()
#sql model
class Product(BaseModel):#serializer
    id:int
    name:str
    description: str
    price: float
    discount: bool


@app.get("/")
def index():
    return {"name":"test fastapi setup"}

@app.get("/greet/")
#greeting
def greet_optional_name(name:Optional[str] = "user"):
    return {"greeting": f"Hi Software Developer {name}"}    
#put
@app.post("/products/")
def post_product(product:Product):
    return product

@app.put("/products/{product_id}")
def update_product(product:Product, product_id: int):
    return {
        "name":product.name,
        "description": product.description,
        "price":product.price,
        "discount":product.discount
    }