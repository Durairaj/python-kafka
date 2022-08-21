from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Stock(BaseModel):
    name: str
    price: float
    symbol: str
    news: str    

@app.get("/")
def read_root():
    return {"app": "twitter_stock_app"}

@app.post("/stocks")
def add_stock(stock:Stock):
    print("Adding stock ", stock.name)
    

@app.get("/stocks/{stock_symbol}")
def get_stock(stock_symbol:str):
    print("Getting stock ", stock_symbol)
    

@app.put("/stocks/{stock_symbol}")
def update_stock(stock_symbol:str):
    print("Updating stock ", stock_symbol)