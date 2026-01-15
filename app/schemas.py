from pydantic import BaseModel, Field
from typing import Optional

class AddressCreate(BaseModel):
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    name: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None

class AddressResponse(AddressCreate):
    id: int

    class Config:
        from_attributes = True
