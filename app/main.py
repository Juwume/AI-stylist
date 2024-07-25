from fastapi import FastAPI
from app.routers import conversation, utils


app = FastAPI()

app.include_router(conversation.router)
app.include_router(utils.router)
