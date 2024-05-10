from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import db_service
from .database import get_db
from .schemas import InventoryBase

router = APIRouter()

@router.post("/inventory", response_model=InventoryBase)
def create_inventory_item(item: InventoryBase, db: Session = Depends(get_db)):
    new_inventory = db_service.create_inventory_item(db, item.dict())
<<<<<<< HEAD
    return InventoryBase.from_orm(new_inventory)
=======
<<<<<<< HEAD
    return InventoryBase.from_orm(new_inventory)
=======
    InventoryBase.from_orm(new_inventory)
>>>>>>> 4e1b3a02e38843ddb007754d6e5bfad7e768a1c6
>>>>>>> 7f2b63ad653ad7ce92b9efa68309b58d5a9ce1df

@router.get("/inventory", response_model=List[InventoryBase])
def list_inventory(db: Session = Depends(get_db)):
    return db_service.get_all_inventory(db)

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======

>>>>>>> 4e1b3a02e38843ddb007754d6e5bfad7e768a1c6
>>>>>>> 7f2b63ad653ad7ce92b9efa68309b58d5a9ce1df
