from fastapi import APIRouter, HTTPException
import requests
from resource.market.market_service import get_market_prices

router = APIRouter()

@router.get("/prices")
def get_prices():
    try:
        return get_market_prices()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
