from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Product, Log
from schemas import ProductCreate
from dependencies import get_db

router = APIRouter()

@router.post("/")
def create_product(product:ProductCreate, db:Session = Depends(get_db)):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    log = Log(action="Product Created", product_id=new_product.id)
    db.add(log)
    db.commit()

    return new_product

@router.get("/")
def get_products(page:int=1, limit:int=5, category:str=None, db:Session=Depends(get_db)):
    query = db.query(Product)

    if category:
        query = query.filter(Product.category == category)

    products = query.offset((page-1)*limit).limit(limit).all()
    return products

@router.get("/{product_id}")
def get_product(product_id:int, db:Session=Depends(get_db)):
    product = db.query(Product).filter(Product.id==product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}")
def update_product(product_id:int, product:ProductCreate, db:Session=Depends(get_db)):
    db_product = db.query(Product).filter(Product.id==product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in product.dict().items():
        setattr(db_product, key, value)

    db.commit()

    log = Log(action="Product Updated", product_id=product_id)
    db.add(log)
    db.commit()

    return db_product

@router.delete("/{product_id}")
def delete_product(product_id:int, db:Session=Depends(get_db)):
    product = db.query(Product).filter(Product.id==product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()

    log = Log(action="Product Deleted", product_id=product_id)
    db.add(log)
    db.commit()

    return {"message":"Product deleted"}