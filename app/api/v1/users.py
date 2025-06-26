from fastapi import APIRouter

router = APIRouter()

@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"id": user_id}
