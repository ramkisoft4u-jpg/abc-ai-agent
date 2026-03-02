from sqlalchemy.orm import Session
from app.models.order import Order
from datetime import datetime


def create_order_record(
    db: Session,
    prod_sale_use_num: int,
    quantity: float,
    reservation_id: int,
) -> Order:
    order = Order(
        manufacturer_cust_ship_to_xref_id=None,
        ordering_physician_id=None,
        location_number=None,
        infusion_type_id=None,
        treatment_plan_id=None,
        treatment_infusion_id=None,
        quantity=quantity,
        calibration_timestamp=datetime.utcnow(),
        order_number="",
        customer_order_number=None,
        delivery_timestamp=None,
        published_timestamp=None,
        row_add_stp=datetime.utcnow(),
        row_add_user_id="AI_AGENT",
        row_update_stp=datetime.utcnow(),
        row_update_user_id="AI_AGENT",
        prod_sale_use_num=prod_sale_use_num,
        pharmacy_order_status=None,
        status=None,
        is_order_rejected=False,
        manufacturer_prod_sale_use_xref_id=None,
        prod_cycle_id=None,
        is_draft_order=False,
        is_order_returned=False,
        reason_cde=None,
        reservation_id=reservation_id,
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
