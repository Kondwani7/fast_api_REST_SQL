from fastapi import FastAPI,status, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from database import SessionalLocal
import models
app = FastAPI()
#sql model
class Product(BaseModel):#serializer
    id:int
    name:str
    description: str
    price: float
    discount: bool
    #serialize to json
    class Config:
        orm_mode = True

db = SessionalLocal()
'''
using our api to make changes in the db
'''
#get all products
@app.get('/products', response_model=List[Product], status_code=200)
def get_all_items():
    products = db.query(models.Product).all()
    return products
#get a product by id
@app.get('/product/{product_id}', 
response_model=Product, status_code=status.HTTP_200_OK)
def get_a_product(product_id:int):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    return product
#create a new product
@app.post('/products', response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product:Product):
   
    #prevent entering a duplicate product
    db_product = db.query(models.Product).filter(
        models.Product.name == product.name).first()
    
    if db_product is not None:
        raise HTTPException(status_code=400, detail="Product already exists")

    
    new_product= models.Product(
        name = product.name,
        description = product.description,
        price = product.price,
        discount = product.discount
    )
    
    db.add(new_product)
    db.commit()
#update a product
@app.put('/product/{product_id}', response_model=Product, status_code=status.HTTP_200_OK)
def update_product(product_id:int, product:Product):
    product_to_update = db.query(models.Product).filter(models.Product.id == product.id).first()
    product_to_update.name = product.name
    product_to_update.description = product.description
    product_to_update.price = product.price
    product_to_update.discount = product.discount

    db.commit()
    return product_to_update
#delete a product
@app.delete('/product/{product_id}')
def delete_product(product_id:int):
    product_to_delete = db.query(models.Product).filter(models.Product.id==product_id).first()

    if product_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details="Product not found")

    db.delete(product_to_delete)
    db.commit()

    return product_to_delete


