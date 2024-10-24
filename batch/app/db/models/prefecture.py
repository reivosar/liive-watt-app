from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base import Base

class Prefecture(Base):
    __tablename__ = 'prefectures'

    code = Column(String(10), primary_key=True)
    name = Column(String(255), nullable=False)

    energy_usages = relationship("EnergyUsage", back_populates="prefecture")