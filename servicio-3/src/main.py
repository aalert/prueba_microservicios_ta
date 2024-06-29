from api.Challenge import router
from fastapi import Depends, FastAPI

app = FastAPI()


app.include_router(
    router.router,
    prefix="/api/challenge",
)
