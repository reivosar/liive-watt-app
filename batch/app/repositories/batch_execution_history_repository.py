from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from app.db.models.batch_execution_history import BatchExecutionHistory
from app.models.batch_execution_status import BatchExecutionStatus

class BatchExecutionHistoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def log_execution_history(self, batch_id: int, status: BatchExecutionStatus, message: str = None) -> BatchExecutionHistory:
        execution_history = BatchExecutionHistory(
            batch_id=batch_id,
            status=status,
            started_at=func.now(),
            message=message
        )
        self.db.add(execution_history)
        self.db.commit()
        return execution_history

    def update_execution_history(self, execution_id: int, status: BatchExecutionStatus, message: str = None):
        execution_history = self.db.query(BatchExecutionHistory).filter(BatchExecutionHistory.id == execution_id).first()
        if execution_history:
            execution_history.finished_at = func.now()
            execution_history.status = status
            execution_history.message = message
            self.db.commit()
