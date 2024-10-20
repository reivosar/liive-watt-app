from app.db.models.batch_management import BatchManagement
from app.repositories.batch_management_repository import BatchManagementRepository

class BatchManagementService:

    def __init__(self, repository: BatchManagementRepository):
        self.repository = repository

    def get_active_batch_by_name(self, batch_name: str) -> BatchManagement:
        job = self.repository.get_active_batch_by_name(batch_name)

        if not job:
            raise ValueError(f"Active batch with name '{batch_name}' not found.")
        
        if job.status.is_inactive:
            raise ValueError(f"Job '{batch_name}' is not active.")
        
        return job
