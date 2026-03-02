from typing import Dict, Any
from app.tools.abc_api_tools import unhold_product_reservation_tool


def reservation_node(state: Dict[str, Any]) -> Dict[str, Any]:
    reservation_id = state.get("reservation_id")
    prod_sale_use_num = state.get("prod_sale_use_num") or state.get("product_id")

    if not reservation_id or not prod_sale_use_num:
        state["messages"].append("Missing reservationId or product for deletion.")
        return state

    resp = unhold_product_reservation_tool.run(
        reservation_id=int(reservation_id),
        prod_sale_use_num=int(prod_sale_use_num),
    )
    state["messages"].append(f"Reservation unheld/deleted: {resp}")
    return state
