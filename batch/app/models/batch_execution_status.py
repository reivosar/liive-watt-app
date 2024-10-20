from enum import Enum

class BatchExecutionStatus(Enum):
    running = 'running'
    success = 'success'
    failed = 'failed'