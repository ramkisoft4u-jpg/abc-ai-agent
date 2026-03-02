from sqlalchemy import Column, BigInteger, Integer, Numeric, Boolean, String, DateTime
from sqlalchemy.sql import func
from app.database import Base


class Order(Base):
    __tablename__ = "order"
    __table_args__ = {"schema": "abc"}

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    manufacturer_cust_ship_to_xref_id = Column(BigInteger, nullable=True)
    ordering_physician_id = Column(BigInteger, nullable=True)
    location_number = Column(BigInteger, nullable=True)
    infusion_type_id = Column(BigInteger, nullable=True)
    treatment_plan_id = Column(BigInteger, nullable=True)
    treatment_infusion_id = Column(BigInteger, nullable=True)
    quantity = Column(Numeric(20, 10), nullable=False, default=0)
    calibration_timestamp = Column(DateTime, nullable=False, server_default=func.now())
    order_number = Column(String(255), nullable=False, default="")
    customer_order_number = Column(BigInteger, nullable=True)
    delivery_timestamp = Column(DateTime, nullable=True)
    published_timestamp = Column(DateTime, nullable=True)
    row_add_stp = Column(DateTime, nullable=False, server_default=func.now())
    row_add_user_id = Column(String(255), nullable=False, default="SYSTEM")
    row_update_stp = Column(DateTime, nullable=False, server_default=func.now())
    row_update_user_id = Column(String(255), nullable=False, default="SYSTEM")
    prod_sale_use_num = Column(BigInteger, nullable=True)
    pharmacy_order_status = Column(BigInteger, nullable=True)
    status = Column(BigInteger, nullable=True)
    is_order_rejected = Column(Boolean, nullable=True)
    manufacturer_prod_sale_use_xref_id = Column(BigInteger, nullable=True)
    prod_cycle_id = Column(BigInteger, nullable=True)
    is_draft_order = Column(Boolean, nullable=True)
    is_order_returned = Column(Boolean, nullable=False, default=False)
    reason_cde = Column(BigInteger, nullable=True)

    # extra column to link reservation (not in original DDL, but useful)
    reservation_id = Column(BigInteger, nullable=True)
