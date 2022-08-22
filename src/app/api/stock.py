from fastapi import APIRouter

router = APIRouter()

class Stock(BaseModel):
    name: str
    price: float
    symbol: str
    news: str    

@router.get("/")
async def read_root():
    return {"app": "twitter_stock_app"}

@router.post("/stocks")
async def add_stock(stock:Stock):
    print("Adding stock ", stock.name)
    

@router.get("/stocks/{stock_symbol}")
async def get_stock(stock_symbol:str):
    print("Getting stock ", stock_symbol)
    

@router.put("/stocks/{stock_symbol}")
async def update_stock(stock_symbol:str):
    print("updating  stock ", stock_symbol)
