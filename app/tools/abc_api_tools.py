import requests
from langchain.tools import tool
from app.config import settings


def _auth_headers():
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.SMP_API_BEARER_TOKEN}",
    }


@tool("get_doses_available", return_direct=False)
def get_doses_available_tool(prod_sale_use_num: str, start_date: str, end_date: str) -> str:
    """
    Wraps GET demand planning dose availability.
    Assumes endpoint like:
    GET /demand-planning/{prodSaleUseNum}/doses-available?startDate=&endDate=
    """
    url = f"{settings.SMP_API_BASE_URL}/demand-planning/{prod_sale_use_num}/doses-available"
    params = {"startDate": start_date, "endDate": end_date}
    resp = requests.get(url, headers=_auth_headers(), params=params, timeout=10)
    if resp.status_code != 200:
        return f"Error {resp.status_code}: {resp.text}"
    return resp.text


@tool("create_product_reservation", return_direct=False)
def create_product_reservation_tool(prod_sale_use_num: int, date: str) -> str:
    """
    Wraps POST demand planning product reservations.
    POST /demand-planning/{prodSaleUseNum}/reservations
    Body: ProductReservationRequest (simplified here).
    """
    url = f"{settings.ABC_API_BASE_URL}/demand-planning/{prod_sale_use_num}/reservations"
    payload = {
        "date": date,
    }
    resp = requests.post(url, headers=_auth_headers(), json=payload, timeout=10)
    if resp.status_code not in (200, 201):
        return f"Error {resp.status_code}: {resp.text}"
    return resp.text


@tool("unhold_product_reservation", return_direct=False)
def unhold_product_reservation_tool(reservation_id: int, prod_sale_use_num: int) -> str:
    """
    Wraps DELETE demand planning unhold reservations.
    DELETE /demand-planning/reservations/{reservationId}/product/{prodSaleUseNum}
    """
    url = f"{settings.ABC_API_BASE_URL}/demand-planning/reservations/{reservation_id}/product/{prod_sale_use_num}"
    resp = requests.delete(url, headers=_auth_headers(), timeout=10)
    if resp.status_code != 200:
        return f"Error {resp.status_code}: {resp.text}"
    return resp.text
