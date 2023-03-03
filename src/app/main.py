from fastapi import FastAPI
from app.api import ping, slack

app = FastAPI()

app.include_router(ping.router)
app.include_router(slack.router)
