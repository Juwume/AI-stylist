from fastapi import FastAPI
from app.routers import conversation


app = FastAPI()

app.include_router(conversation.router)
