from fastapi import APIRouter
from .hello import router as hello_router

router = APIRouter()

router.include_router(hello_router, tags=["hello"])
