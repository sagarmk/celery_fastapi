from fastapi import FastAPI
from app.worker import delivery_date
from app.model import Delivery


app = FastAPI()

@app.post('/order')
def add_order(delivery: Delivery):
    delivery_date.delay(delivery.customer_name, delivery.order_number)
    return {"message": "Calculating order delivery date"}

@app.get("/")
async def root():
    return {"message": "Status: Active"}