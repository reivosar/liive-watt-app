import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.connection import session_scope
from app.repositories.batch_execution_history_repository import BatchExecutionHistoryRepository
from app.repositories.batch_management_repository import BatchManagementRepository
from app.services.batch_execution_logger import BatchExecutionLogger
from app.services.batch_management_service import BatchManagementService
from app.models.batch_execution_status import BatchExecutionStatus

def run_job_by_name(batch_name: str, *args):

    with session_scope() as db:

        logger = BatchExecutionLogger(BatchExecutionHistoryRepository(db)) 
        service = BatchManagementService(BatchManagementRepository(db))

        try:
            job = service.get_active_batch_by_name(batch_name)
        except ValueError as e:
            print(str(e))
            return

        execution_history = logger.log_execution_history(job.id, BatchExecutionStatus.running)

        try:
            module = importlib.import_module(job.module_path)
            
            if job.class_name:
                class_ = getattr(module, job.class_name)
                instance = class_() 
                
                if args:
                    getattr(instance, job.function_name)(*args) 
                else:
                    getattr(instance, job.function_name)()
            else:
                function = getattr(module, job.function_name)
                
                if args:
                    function(*args) 
                else:
                    function()

            logger.update_execution_history(execution_history.id, BatchExecutionStatus.success)
        except Exception as e:
            logger.update_execution_history(execution_history.id, BatchExecutionStatus.failed, str(e))
            print(f"Error running job '{batch_name}': {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_job.py <batch_name> [<args>...]")
        sys.exit(1)
    
    batch_name = sys.argv[1]
    args = sys.argv[2:]

    run_job_by_name(batch_name, *args)
