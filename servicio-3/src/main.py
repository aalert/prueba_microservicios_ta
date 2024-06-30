from api import Challenge
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"status": "No se pudo procesar los párametros"},
    )

app.include_router(
    Challenge.router,
    prefix="/api/challenge",
)
