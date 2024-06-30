from datetime import datetime as datetime_t
from typing import Optional

from pydantic import BaseModel

from connections.models import AlertType


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
    type: Optional[AlertType] = None
    sended: bool
    created_at: datetime_t
    updated_at: datetime_t


class Search(BaseModel):
    version: int
    type: Optional[AlertType] = None
    sended: Optional[bool] = None
    class Config:
        extra = "forbid"

class SendAlert(BaseModel):
    version: int
    type: Optional[AlertType] = None

    class Config:
        extra = "forbid"