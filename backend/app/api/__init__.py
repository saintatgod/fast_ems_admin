from fastapi import APIRouter
from .system import system_router

ApiRouter = APIRouter()
ApiRouter.include_router(system_router, prefix="/system")