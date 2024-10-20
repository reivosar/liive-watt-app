from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .base import Base

class EnergyUsage(Base):
    __tablename__ = 'energy_usages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    prefecture_code = Column(String(10), ForeignKey('prefectures.code', ondelete='CASCADE'), nullable=False)
    consumption = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    recorded_at = Column(TIMESTAMP, default="NOW()")

    prefecture = relationship("Prefecture", back_populates="energy_usages")
