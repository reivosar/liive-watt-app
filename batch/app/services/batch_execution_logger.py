from app.db.models.batch_execution_history import BatchExecutionHistory
from app.models.batch_execution_status import BatchExecutionStatus
from app.repositories.batch_execution_history_repository import BatchExecutionHistoryRepository

class BatchExecutionLogger:

    def __init__(self, repository: BatchExecutionHistoryRepository):
        self.repository = repository

    def log_execution_history(self, batch_id: int, status: BatchExecutionStatus, message: str = None) -> BatchExecutionHistory:
        execution_history = self.repository.log_execution_history(batch_id, status, message)
        return execution_history

    def update_execution_history(self, execution_id: int, status: BatchExecutionStatus, message: str = None):
        self.repository.update_execution_history(execution_id, status, message)