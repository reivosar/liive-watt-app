from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import ENUM
from .base import Base
from app.models.batch_management_status import BatchManagementStatus

class BatchManagement(Base):
    __tablename__ = 'batch_management'

    id = Column(Integer, primary_key=True, index=True)
    batch_name = Column(String(255), nullable=False)
    module_path = Column(String(255), nullable=False)
    class_name = Column(String(255))
    function_name = Column(String(255), nullable=False)
    status = Column(ENUM(BatchManagementStatus, name="batch_management_status", create_type=False), nullable=False, default=BatchManagementStatus.active)
    last_run_at = Column(TIMESTAMP)