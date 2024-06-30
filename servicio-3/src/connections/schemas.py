from datetime import datetime as datetime_t
from typing import Optional

from connections.models import AlertType
from pydantic import BaseModel


class ProcessDevices(BaseModel):
    version: int
    timeSearch: str

class Device(BaseModel):
    time: datetime_t
    value: float
    version: int


class Alert(BaseModel):
    id_alerta: Optional[int]
    datetime: datetime_t
    value: float
    version: int
    type: AlertType
    sended: bool
    created_at: datetime_t
    updated_at: datetime_t


