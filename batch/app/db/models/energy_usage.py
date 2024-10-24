from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Numeric
from sqlalchemy.orm import relationship
from .base import Base

class EnergyUsage(Base):
    __tablename__ = 'energy_usages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    prefecture_code = Column(String(10), ForeignKey('prefectures.code', ondelete='CASCADE'), nullable=False)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    special_high_voltage_consumption = Column(Numeric, nullable=True)
    special_high_voltage_retailers_count = Column(Numeric, nullable=True)
    high_voltage_consumption = Column(Numeric, nullable=True)
    high_voltage_retailers_count = Column(Numeric, nullable=True)
    low_voltage_consumption = Column(Numeric, nullable=True)
    low_voltage_special_demand = Column(Numeric, nullable=True)
    low_voltage_free_pricing = Column(Numeric, nullable=True)
    low_voltage_retailers_count = Column(Numeric, nullable=True)
    total_consumption = Column(Numeric, nullable=True)
    total_retailers_count = Column(Numeric, nullable=True)
    recorded_at = Column(TIMESTAMP, default="NOW()")

    prefecture = relationship("Prefecture", back_populates="energy_usages")
