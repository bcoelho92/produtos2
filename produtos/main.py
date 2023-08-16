from fastapi import FastAPI
import produtos.models as models_db
from produtos.routes import router_user, router_favorites, router_products
from produtos.database import engine

# models.Base.metadata.drop_all(bind=engine)
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router_user, prefix="/users", tags=["Users"])
app.include_router(router_products, prefix="/products", tags=["Products"])
app.include_router(router_favorites, prefix="/favorites", tags=["Favorites"])