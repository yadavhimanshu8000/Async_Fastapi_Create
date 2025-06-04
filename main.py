from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import SessionLocal, engine
from sqlalchemy.future import select

from service import models  
from urls.v1 import(
    user
)

app = FastAPI(
        title="User_Details",
        description="Fastapi",
        version="1.0.0",
        contact={
        "name": "Himanshu",
        "url": "https://your-website.com",
        "email": "himanshu@gmail.com"
        },
        license_info={
            "name": "Softedge",
            "url": "https://opensource.org/licenses/Softedge",
        },
        terms_of_service="https://www.example.com/terms",
        docs_url='/docs',
    )

# Create tables asynchronously
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

# Run this at startup
@app.on_event("startup")
async def on_startup():
    await init_models()


@app.get("/")
async def root():
    return {"message": "User_details_Fastapi"}


app.include_router(user.router,tags=["Users"])

