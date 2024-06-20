""" Alert Model """
# from db.models.model_base import Base

# class Alert(Base):
#     __tablename__ = "alerts"
from pydantic import BaseModel

class Alert(BaseModel):
    name: str
    symbol: str
    threshold: float
    current_price: float
    message: str
