from fastapi import FastAPI
from database import engine, Base
from routers import auth, products

app = FastAPI(title="Product Management API")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(products.router, prefix="/products", tags=["Products"])