from fastapi import FastAPI
from app.routers import *
from .db.init_db import init_db

init_db()

app = FastAPI()

app.include_router(bug.router, prefix="/bugs", tags=["Bug"])