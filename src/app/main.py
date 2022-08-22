from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

app.include_router(stock.router)
    print("Updating stock ", stock_symbol)