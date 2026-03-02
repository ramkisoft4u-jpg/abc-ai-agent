from pydantic import BaseModel
from typing import Optional, List, Any, TypedDict


class ChatRequest(BaseModel):
    query: str
    use_rag: bool = True


class WorkflowState(TypedDict):
    user_query: str
    intent: Optional[str]
    product_id: Optional[str]
    prod_sale_use_num: Optional[int]
    date: Optional[str]
    quantity: Optional[float]
    reservation_id: Optional[int]
    order_id: Optional[int]
    messages: List[str]
