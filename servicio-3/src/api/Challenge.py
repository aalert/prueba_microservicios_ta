
import helpers
from connections import crud, influx_adapter, models, schemas
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=models.engine)
router = APIRouter()

def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/process")
async def process(devices: schemas.ProcessDevices, db: Session = Depends(get_db)):
    """
    body
    "version": number,
    "timeSearch": string (eg:"15m, 3h, 2d")


    responses
    - 200 `{"status": "ok"}`
    - 422 `{"status": "No se pudo procesar los párametros"}`
    - 500 `{"status": "Error: {motivo}"}`
    """
    try:
        absolute_time = helpers.parse_absolute_time(devices.timeSearch)
    except Exception:
        return JSONResponse(content={"status": "No se pudo procesar los párametros"}, status_code=422)

    try:
        devices = influx_adapter.read_devices_from_system(
            absolute_time, devices.version
        )

        alerts = list(map(helpers.create_alert_form_device, devices))

        crud.insert_alerts(db, alerts)

        return JSONResponse(content={"status": "ok"})
    except Exception as e:
        return JSONResponse(content={"status": f"Error: {str(e)}"}, status_code=500)


@router.post("/search")
async def search(search: schemas.Search, db: Session = Depends(get_db)):
    """
    Search alerts in the database filtered by the parameters in the body
    where type and sended are optional

    body
    "version": number,
    "type": string, // opcional
    "sended": bool // opcional

    response
    [
        {
            datetime: "2022-01-01 10:00:01",
            value: 566.45,
            version: 1,
            type: "MEDIA",
            sended: false
        }, ...
    ]
    """

    alerts = crud.search_alerts(db, search)

    return alerts

@router.post("/send")
async def send(send_alerts: schemas.SendAlert, db: Session = Depends(get_db)):
    """
    Send all unsended alerts filtered by version and type

    body
    "version": number
    "type": string

    Reponse
    - 200 `{"status": "ok"}`
    - 422 `{"status": "No se pudo procesar los párametros"}`
    - 500 `{"status": "Error: {motivo}"}`
    """

    try:
        crud.send_alerts(db, send_alerts)
        return JSONResponse(content={"status": "ok"})
    except Exception as e:
        return JSONResponse(content={"status": f"Error: {str(e)}"}, status_code=500)