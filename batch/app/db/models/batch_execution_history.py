from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, TIMESTAMP, Text, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM
from .base import Base
from app.models.batch_execution_status import BatchExecutionStatus

class BatchExecutionHistory(Base):
    __tablename__ = 'batch_execution_history'

    id = Column(Integer, primary_key=True, autoincrement=True)
    batch_id = Column(Integer, ForeignKey('batch_management.id'), nullable=False) 
    status = Column(ENUM(BatchExecutionStatus, name="batch_execution_status", create_type=False), nullable=False, default=BatchExecutionStatus.running) 
    started_at = Column(TIMESTAMP, server_default=func.now()) 
    finished_at = Column(TIMESTAMP)
    message = Column(Text)
