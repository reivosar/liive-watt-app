from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app.db.models.batch_management import BatchManagement

class BatchManagementRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_active_batch_by_name(self, batch_name: str) -> BatchManagement:
        try:
            return self.db.query(BatchManagement).filter(
                BatchManagement.batch_name == batch_name,
            ).one()
        except NoResultFound:
            return None