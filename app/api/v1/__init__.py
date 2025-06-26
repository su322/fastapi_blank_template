from fastapi import APIRouter
from app.api.v1 import users, auth

router = APIRouter()

router.include_router(users.router, prefix="/users")
router.include_router(auth.router, prefix="/auth")
