from fastapi import FastAPI
from contextlib import asynccontextmanager
from datetime import datetime

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting app : ", datetime.now())
    yield
    print("Stopping app: ", datetime.now())