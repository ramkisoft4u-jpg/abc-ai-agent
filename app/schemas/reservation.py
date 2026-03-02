from pydantic import BaseModel


class ReservationRequest(BaseModel):
    prod_sale_use_num: int
    date: str
