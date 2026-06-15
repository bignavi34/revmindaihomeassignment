from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.products import router as products_router
from app.api.summary import router as summary_router
from app.api.trends import router as trends_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    products_router,
    prefix="/api",
    tags=["Products"],
)
app.include_router(
    summary_router,
    prefix="/api",
    tags=["Summary"],
)
app.include_router(
    trends_router,
    prefix="/api",
    tags=["Trends"]
)
from app.api.chat import (
    router as chat_router
)

app.include_router(
    chat_router,
    prefix="/api",
    tags=["Chat"]
)

@app.get("/")
async def root():
    return {"message": "NovaBite API is running"}