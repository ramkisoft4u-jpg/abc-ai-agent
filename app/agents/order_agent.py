from typing import Dict, Any
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.order import Order
from app.tools.mysql_tools import create_order_record
from app.tools.abc_api_tools import unhold_product_reservation_tool


def order_node(state: Dict[str, Any]) -> Dict[str, Any]:
    reservation_id = state.get("reservation_id")
    prod_sale_use_num = state.get("prod_sale_use_num")
    date = state.get("date")
    quantity = state.get("quantity") or 1

    if not reservation_id or not prod_sale_use_num or not date:
        state["messages"].append("Missing data to create order.")
        return state

    db: Session = SessionLocal()
    try:
        order: Order = create_order_record(
            db=db,
            prod_sale_use_num=int(prod_sale_use_num),
            quantity=float(quantity),
            reservation_id=int(reservation_id),
        )
        state["order_id"] = order.id

        unhold_resp = unhold_product_reservation_tool.run(
            reservation_id=int(reservation_id),
            prod_sale_use_num=int(prod_sale_use_num),
        )
        state["messages"].append(f"Reservation released: {unhold_resp}")
    except Exception as e:
        db.rollback()
        state["messages"].append(f"Order creation failed: {e}")
    finally:
        db.close()

    return state
