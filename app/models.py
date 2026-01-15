from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    name = Column(String, nullable=True)
    street = Column(String, nullable=True)
    city = Column(String, nullable=True)
