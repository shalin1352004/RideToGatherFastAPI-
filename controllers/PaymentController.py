from models.PaymentModel import Payment

from config.database import payments_collection

async def create_payment(payment:Payment):
    payment_dict = payment.dict()
    result = await payments_collection.insert_one(payment_dict)
    
    return {"payment_id": str(result.inserted_id), "message": "Payment created successfully"  }         

def convert_id(payment):
    payment["_id"] = str(payment["_id"])
    return payment  

async def get_payments(min_amount:float):
    query = {"amount": {"$gte": min_amount}}
    cursor = await payments_collection.find(query).to_list(length=100)
    return [convert_id(payment) for payment in cursor]

async def get_all_payments():
    cursor = await payments_collection.find().to_list(length=100)
    return [Payment(**payment) for payment in cursor]          