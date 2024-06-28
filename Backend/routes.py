import datetime
from datetime import datetime
from fastapi import APIRouter, HTTPException, Form, Body
from typing import List
from database import products_collection
from models import Product

router = APIRouter()

@router.post("/api/products/", response_model=Product)
async def create_product(name: str = Form(...), description: str = Form(...), quantity: int = Form(...)):
    new_product = Product(name=name, description=description, quantity=quantity)
    result = await products_collection.insert_one(new_product.dict())
    created_product = await products_collection.find_one({"_id": result.inserted_id})
    return Product(**created_product)

@router.get("/api/products/", response_model=List[Product])
async def get_products():
    products = await products_collection.find({}).to_list(length=100)
    return [Product(**product) for product in products]

@router.get("/api/products/{product_name}", response_model=Product)
async def get_product(product_name: str):
    product = await products_collection.find_one({"name": product_name})
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return Product(**product)


@router.put("/api/products/{product_name}/purchase", response_model=Product)
async def purchase_product(product_name: str, quantity: int = Body(..., embed=True)):
    product_from_db = await products_collection.find_one({"name": product_name})
    if product_from_db is None:
        raise HTTPException(status_code=404, detail="Product not found")

    product = Product(**product_from_db)
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be positive")

    if quantity > product.quantity:
        raise HTTPException(status_code=400, detail="Not enough quantity available")

    product.subtract_from_quantity(quantity)
    product.save_analysis(time=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), quantity=quantity)
    await products_collection.update_one({"name": product_name}, {"$set": product.dict()})
    return product


@router.get("/api/products/{product_name}/analysis")
async def get_product_analysis(product_name: str):
    product_from_db = await products_collection.find_one({"name": product_name})
    product = Product(**product_from_db)
    return product.analysis


@router.delete("/api/products/{product_name}")
async def delete_product(product_name: str):
    product_from_db = await products_collection.find_one({"name": product_name})
    if not product_from_db:
        raise HTTPException(status_code=404, detail="Product not found")

    await products_collection.delete_one({"name": product_name})
    return {"message": "Product Successfully Deleted"}
