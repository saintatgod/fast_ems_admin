from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import json


class EnforceJSONMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 检查请求的内容类型是否为 application/json
        content_type = request.headers.get('Content-Type', '')
        if not content_type.startswith('application/json'):
            return Response(
                content="Request body must be JSON.",
                status_code=415,  # Unsupported Media Type
                media_type="text/plain"
            )

        # 检查请求体是否为空
        if not await request.body():
            return Response(
                content="Request body must not be empty.",
                status_code=400,  # Bad Request
                media_type="text/plain"
            )

        # 尝试解析请求体为 JSON
        try:
            await request.json()
        except json.JSONDecodeError:
            return Response(
                content="Request body must be valid JSON.",
                status_code=400,  # Bad Request
                media_type="text/plain"
            )

        # 继续处理请求
        return await call_next(request)