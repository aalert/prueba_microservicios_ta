from typing import List

from sqlalchemy.orm import Session

from connections import schemas
from connections.models import Alerts


# insert list of alerts into table Alerts
def insert_alerts(db: Session, alerts: List[schemas.Alert]):
    """
    alerts must be a list of Alerts objects
    """
    alerts_objects = map(lambda alert: Alerts(**alert.model_dump()), alerts)

    db.bulk_save_objects(alerts_objects)
    db.commit()

def search_alerts(db: Session, search: schemas.Search) -> List[Alerts]:
    """
    search alerts in the database filtered by the parameters in the body
    where type and sended are optional
    """
    query = db.query(Alerts).filter(Alerts.version == search.version)

    if search.type:
        query = query.filter(Alerts.type == search.type.upper())

    if search.sended is not None:
        query = query.filter(Alerts.sended == search.sended)

    return list(query.all())
