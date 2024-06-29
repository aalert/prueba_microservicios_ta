from datetime import datetime as datetime_t

from pydantic import BaseModel

from connections.models import AlertType


class ProcessDevices(BaseModel):
    version: int
    timeSearch: str


class Alert(BaseModel):
    id_alerta: int
    datetime: datetime_t
    value: float
    version: int
    type: AlertType
    sended: bool
    created_at: datetime_t
    updated_at: datetime_t

    def create_alert_form_device(device: ProcessDevices):
        return Alert(
            id_alerta=None,
            datetime=device.time,
            value=device.value,
            version=device.version,
            sended=False,
            type=Alert.calculate_tyoe(device.version, device.value),
            created_at=datetime_t.now(),
            updated_at=datetime_t.now(),
        )

    def calculate_tyoe(version: int, value: float) -> AlertType:

        if version == 1:
            if value > 800:
                return AlertType.ALTA
            elif value > 500:
                return AlertType.MEDIA
            elif value > 200:
                return AlertType.BAJA
        elif version == 2:
            if value < 200:
                return AlertType.ALTA
            elif value < 500:
                return AlertType.MEDIA
            elif value < 800:
                return AlertType.BAJA


