from sqlalchemy import Column, Integer, String, Float
from db.model_base import Base

class AlertRule(Base):
    __tablename__ = "alert_rules"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    threshold = Column(Float)
    symbol = Column(String)
