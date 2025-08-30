from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from typing import List, Optional
import uvicorn
import os
from dotenv import load_dotenv

from database import engine, get_db
from models import Base
from schemas import *
from crud import *

# Load environment variables
load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mahadeva Electronics API",
    description="FastAPI backend for Mahadeva Electronics website",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="."), name="static")

# API Routes

@app.get("/")
async def root():
    return {"message": "Mahadeva Electronics API"}

# Product routes
@app.get("/api/products/", response_model=List[ProductResponse])
async def get_products(db: Session = Depends(get_db)):
    return get_all_products(db)

@app.post("/api/products/", response_model=ProductResponse)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_new_product(db, product)

@app.get("/api/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/api/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    updated_product = update_existing_product(db, product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@app.delete("/api/products/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    success = delete_existing_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

# Part routes
@app.get("/api/parts/", response_model=List[PartResponse])
async def get_parts(db: Session = Depends(get_db)):
    return get_all_parts(db)

@app.post("/api/parts/", response_model=PartResponse)
async def create_part(part: PartCreate, db: Session = Depends(get_db)):
    return create_new_part(db, part)

@app.get("/api/parts/{part_id}", response_model=PartResponse)
async def get_part(part_id: int, db: Session = Depends(get_db)):
    part = get_part_by_id(db, part_id)
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    return part

@app.put("/api/parts/{part_id}", response_model=PartResponse)
async def update_part(part_id: int, part: PartUpdate, db: Session = Depends(get_db)):
    updated_part = update_existing_part(db, part_id, part)
    if not updated_part:
        raise HTTPException(status_code=404, detail="Part not found")
    return updated_part

@app.delete("/api/parts/{part_id}")
async def delete_part(part_id: int, db: Session = Depends(get_db)):
    success = delete_existing_part(db, part_id)
    if not success:
        raise HTTPException(status_code=404, detail="Part not found")
    return {"message": "Part deleted successfully"}

# Technician routes
@app.get("/api/technicians/", response_model=List[TechnicianResponse])
async def get_technicians(db: Session = Depends(get_db)):
    return get_all_technicians(db)

@app.post("/api/technicians/", response_model=TechnicianResponse)
async def create_technician(technician: TechnicianCreate, db: Session = Depends(get_db)):
    return create_new_technician(db, technician)

@app.put("/api/technicians/{technician_id}", response_model=TechnicianResponse)
async def update_technician(technician_id: int, technician: TechnicianUpdate, db: Session = Depends(get_db)):
    updated_technician = update_existing_technician(db, technician_id, technician)
    if not updated_technician:
        raise HTTPException(status_code=404, detail="Technician not found")
    return updated_technician

@app.delete("/api/technicians/{technician_id}")
async def delete_technician(technician_id: int, db: Session = Depends(get_db)):
    success = delete_existing_technician(db, technician_id)
    if not success:
        raise HTTPException(status_code=404, detail="Technician not found")
    return {"message": "Technician deleted successfully"}

# Booking routes
@app.get("/api/bookings/", response_model=List[BookingResponse])
async def get_bookings(db: Session = Depends(get_db)):
    return get_all_bookings(db)

@app.post("/api/bookings/", response_model=BookingResponse)
async def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    return create_new_booking(db, booking)

@app.put("/api/bookings/{booking_id}", response_model=BookingResponse)
async def update_booking(booking_id: int, booking: BookingUpdate, db: Session = Depends(get_db)):
    updated_booking = update_existing_booking(db, booking_id, booking)
    if not updated_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return updated_booking

@app.delete("/api/bookings/{booking_id}")
async def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    success = delete_existing_booking(db, booking_id)
    if not success:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"message": "Booking deleted successfully"}

# Feedback routes
@app.get("/api/feedback/", response_model=List[FeedbackResponse])
async def get_feedback(db: Session = Depends(get_db)):
    return get_all_feedback(db)

@app.post("/api/feedback/", response_model=FeedbackResponse)
async def create_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    return create_new_feedback(db, feedback)

@app.put("/api/feedback/{feedback_id}", response_model=FeedbackResponse)
async def update_feedback(feedback_id: int, feedback: FeedbackUpdate, db: Session = Depends(get_db)):
    updated_feedback = update_existing_feedback(db, feedback_id, feedback)
    if not updated_feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return updated_feedback

@app.delete("/api/feedback/{feedback_id}")
async def delete_feedback(feedback_id: int, db: Session = Depends(get_db)):
    success = delete_existing_feedback(db, feedback_id)
    if not success:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return {"message": "Feedback deleted successfully"}

# Authentication routes
@app.post("/api/auth/token/")
async def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, login_data.email, login_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
