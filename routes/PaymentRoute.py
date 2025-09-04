from models.PaymentModel import Payment
from config.database import payments_collection 
from fastapi import APIRouter
from controllers.PaymentController import create_payment, get_payments , get_all_payments                     

router = APIRouter()

@router.post("/create-payments/")
async def add_payment(payment: Payment):
    return await create_payment(payment)

@router.get("/filtered-payments/")
async def fetch_payments(min_amount: float = 0):
    return await get_payments(min_amount)   

@router.get("/all-payments/")
async def fetch_all_payments():
    return await get_all_payments()