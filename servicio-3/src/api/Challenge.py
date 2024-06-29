
from connections import crud, influx_adapter, schemas
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/process")
async def process(devices: schemas.ProcessDevices):
    """
    responses
    - 200 `{"status": "ok"}`
    - 422 `{"status": "No se pudo procesar los párametros"}`
    - 500 `{"status": "Error: {motivo}"}`
    """

    try:
        devices = influx_adapter.read_devices_from_system(
            devices.timeSearch, devices.version
        )

        alerts = map(schemas.Alert.create_alert_form_device, devices)

        crud.insert_alerts(alerts)


        return JSONResponse(content={"status": "ok"})
    except Exception as e:
        return JSONResponse(content={"status": f"Error: {str(e)}"}, status_code=500)

