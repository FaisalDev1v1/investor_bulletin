from fastapi import APIRouter
from api.controllers import market_controller, rules_controller, alerts_controller

router = APIRouter()
router.include_router(market_controller.router, prefix="/market", tags=["market"])
router.include_router(rules_controller.router, prefix="/alert-rules", tags=["alert-rules"])
router.include_router(alerts_controller.router, prefix="/alerts", tags=["alerts"])



































# from fastapi import APIRouter, HTTPException
# import requests

# router = APIRouter()

# API_KEY = "a36fff32b6e84b0b97e7f3d1eb164cf2"
# BASE_URL = "https://twelve-data1.p.rapidapi.com/time_series"

# headers = {
#     "X-RapidAPI-Key": API_KEY,
#     "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
# }

# symbols = ["AAPL", "MSFT", "GOOG", "AMZN", "META"]

# @router.get("/market-prices")
# def get_market_prices():
#     prices = {}
#     for symbol in symbols:
#         response = requests.get(BASE_URL, headers=headers, params={
#             "symbol": symbol,
#             "interval": "1min",
#             "outputsize": "1"
#         })
#         if response.status_code == 200:
#             data = response.json()
#             prices[symbol] = data['values'][0]['close']
#         else:
#             raise HTTPException(status_code=response.status_code, detail="Error retrieving data")
#     return prices

