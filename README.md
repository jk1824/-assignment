# Address Book API

## Description
A FastAPI-based Address Book API that allows users to:
- Create an address
- List all addresses
- Delete an address
- Find nearby addresses using latitude, longitude, and distance

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Geopy

## Setup Instructions
1. Create virtual environment
2. Install dependencies
3. Run the application

## Run Command
uvicorn app.main:app --reload

## API Endpoints
POST /addresses  
GET /addresses  
DELETE /addresses/{id}  
GET /addresses/nearby?latitude=&longitude=&distance_km=

## Sample Request
GET /addresses/nearby?latitude=12.97&longitude=77.59&distance_km=5
