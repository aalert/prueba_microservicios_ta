from api import Challenge
from fastapi import Depends, FastAPI

app = FastAPI()


app.include_router(
    Challenge.router,
    prefix="/api/challenge",
)
