from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from products.routes import router as api_router

app = FastAPI()

app.include_router(api_router, prefix="/api")


