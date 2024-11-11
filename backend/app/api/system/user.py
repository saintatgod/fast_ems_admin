from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.core.response import SuccessResponse,ErrorResponse

router = APIRouter()

@router.get("/info", summary="获取用户信息", description="获取用户信息")
async def get_user_info()->JSONResponse:
    return SuccessResponse(data={"username": "admin", "email": "admin@example.com", "phone": "1234567890", "avatar": "https://example.com/avatar.jpg"})