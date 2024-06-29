from datetime import datetime

from connections.models import AlertType


class Alert:
    def __init__(
        self, datetime: datetime, value: float, version: int,
        type: AlertType | None = None,
        sended: bool=False,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        id_alerta: int | None = None
    ):
        self.id_alerta = id_alerta
        self.datetime = datetime
        self.value = value
        self.version = version
        self.type = type
        self.sended = sended
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return (
            f"Id: {self.id_alerta}, time: {self.datetime},"
            " value: {self.value}, version: {self.version}"
        )

