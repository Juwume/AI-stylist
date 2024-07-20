from fastapi import FastAPI
from .routers import ask, suggest
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(ask.router)
app.include_router(suggest.router)