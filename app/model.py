from pydantic import BaseModel

class Delivery(BaseModel):
    customer_name: str
    order_number: int