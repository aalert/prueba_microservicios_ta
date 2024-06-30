
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

    absolute_time = helpers.parse_absolute_time(devices.timeSearch)
    #try:
    devices = influx_adapter.read_devices_from_system(
        absolute_time, devices.version
    )

    alerts = map(helpers.create_alert_form_device, devices)

    crud.insert_alerts(db, alerts)


        #return JSONResponse(content={"status": "ok"})
    #except Exception as e:
        #return JSONResponse(content={"status": f"Error: {str(e)}"}, status_code=500)

