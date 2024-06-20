""" Alert Rule Schema """
"""_summary_
This file to abstract any validation logic for the Alert Rules
"""
from pydantic import BaseModel

class AlertRule(BaseModel):
    name: str
    threshold: float
    symbol: str

class AlertRuleUpdate(BaseModel):
    name: str = None
    threshold: float = None
    symbol: str = None

