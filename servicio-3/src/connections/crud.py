from typing import List

from sqlalchemy.orm import Session

from connections import schemas
from connections.models import Alerts


# insert list of alerts into table Alerts
def insert_alerts(db: Session, alerts: List[schemas.Alert]):
    """
    alerts must be a list of Alerts objects
    """

    db.bulk_save_objects(alerts)
    db.commit()
