from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import Base, engine, SessionLocal
from app import crud, models, schemas, utils


app = FastAPI(title="Address Book API")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/addresses", response_model=schemas.AddressResponse)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db, address)

@app.get("/addresses", response_model=list[schemas.AddressResponse])
def list_addresses(db: Session = Depends(get_db)):
    return crud.get_all_addresses(db)

@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    address = crud.delete_address(db, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return {"message": "Address deleted successfully"}


@app.get("/addresses/nearby", response_model=List[schemas.AddressResponse])
def get_nearby_addresses(
    latitude: float = Query(..., ge=-90, le=90),
    longitude: float = Query(..., ge=-180, le=180),
    distance_km: float = Query(..., gt=0),
    db: Session = Depends(get_db)
):
    addresses = crud.get_all_addresses(db)
    result = []

    for addr in addresses:
        if utils.is_within_distance(
            latitude,
            longitude,
            addr.latitude,
            addr.longitude,
            distance_km
        ):
            result.append(addr)

    return result

