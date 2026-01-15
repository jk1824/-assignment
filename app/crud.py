from sqlalchemy.orm import Session
from app.models import Address
from app.schemas import AddressCreate

def create_address(db: Session, address: AddressCreate):
    db_address = Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def get_all_addresses(db: Session):
    return db.query(Address).all()

def delete_address(db: Session, address_id: int):
    address = db.query(Address).filter(Address.id == address_id).first()
    if address:
        db.delete(address)
        db.commit()
    return address
