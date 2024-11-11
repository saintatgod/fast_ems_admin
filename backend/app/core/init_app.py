from fastapi import FastAPI, applications
from contextlib import asynccontextmanager
from datetime import datetime
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html

# 定义一个异步上下文管理器，用于启动和停止应用程序
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 打印应用程序启动时间
    print("Starting app : ", datetime.now())
    yield
    # 打印应用程序停止时间
    print("Stopping app: ", datetime.now())

# 重置API文档, 替换swagger和redoc的HTML
def reset_api_docs() -> None:
    # 定义一个函数，用于替换swagger的HTML
    def swagger_monkey_patch(*args, **kwargs):
        return get_swagger_ui_html(
            *args, **kwargs,
            swagger_css_url="/static/swagger/swagger-ui.css",
            swagger_js_url="/static/swagger/swagger-ui-bundle.js",
            swagger_favicon_url="/static/favicon.png"
        )

    # 定义一个函数，用于替换redoc的HTML
    def redoc_monkey_patch(*args, **kwargs):
        return get_redoc_html(
            *args, **kwargs,
            redoc_js_url="/static/swagger/redoc/bundles/redoc.standalone.js",
            redoc_favicon_url="/static/favicon.png"
        )

    # 替换applications中的swagger和redoc函数
    applications.get_swagger_ui_html = swagger_monkey_patch
    applications.get_redoc_html = redoc_monkey_patch