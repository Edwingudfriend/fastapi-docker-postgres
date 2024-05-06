from sqlalchemy.orm import Session
from .models import Order
from sqlalchemy.exc import SQLAlchemyError

def create_order(order_data, db: Session):
    try:
        new_order = Order(**order_data)
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        return new_order
    except SQLAlchemyError as e:
        db.rollback()
        # Log the error or handle it appropriately
        raise e

def get_order_by_id(order_id: int, db: Session):
    try:
        return db.query(Order).filter(Order.id == order_id).first()
    except SQLAlchemyError as e:
        # Log the error or handle it appropriately
        raise e
