from fastapi import FastAPI
from produtos.routes import router_user, router_favorites, router_products

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API favoritos!"}

app.include_router(router_user, prefix="/users", tags=["Users"])
app.include_router(router_products, prefix="/products", tags=["Products"])
app.include_router(router_favorites, prefix="/favorites", tags=["Favorites"])