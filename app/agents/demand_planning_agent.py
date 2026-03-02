from typing import Dict, Any
from app.tools.abc_api_tools import (
    get_doses_available_tool,
    create_product_reservation_tool,
)
from app.utils.date_utils import normalize_date


def demand_planning_node(state: Dict[str, Any]) -> Dict[str, Any]:
    date = normalize_date(state.get("date"))
    state["date"] = date

    prod_sale_use_num = state.get("prod_sale_use_num") or state.get("product_id")
    if not prod_sale_use_num or not date:
        state["messages"].append("Missing product or date for demand planning.")
        return state

    doses = get_doses_available_tool.run(
        prod_sale_use_num=str(prod_sale_use_num),
        start_date=date,
        end_date=date,
    )
    if "No available doses" in doses or "Error" in doses:
        state["messages"].append(f"Dose availability error: {doses}")
        return state

    reservation = create_product_reservation_tool.run(
        prod_sale_use_num=int(prod_sale_use_num),
        date=date,
    )
    import json

    try:
        res_json = json.loads(reservation)
        state["reservation_id"] = res_json.get("id") or res_json.get("reservationId")
    except Exception:
        state["messages"].append(f"Failed to parse reservation response: {reservation}")

    return state
