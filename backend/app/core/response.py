from fastapi.responses import JSONResponse as Response
from fastapi import status
from typing import Any, Optional

class SuccessResponse(Response):
    """
    成功响应
    """
    def __init__(
            self,
            data: Optional[Any] = None,
            msg: Optional[str] = "success",
            code: int = status.HTTP_200_OK,
            status_code: int = status.HTTP_200_OK
    ) -> None:
        self.data = {
            "code": code,
            "data": data,
            "message": msg
        }
        super().__init__(content=self.data, status_code=status_code)


class ErrorResponse(Response):
    """
    失败响应
    """
    def __init__(
            self,
            msg: Optional[str] = None,
            code=status.HTTP_400_BAD_REQUEST,
            status_code=status.HTTP_200_OK
    ) -> None:
        self.data = {
            "code": code,
            "message": msg,
            "data": None
        }
        super().__init__(content=self.data, status_code=status_code)