from pydantic import BaseModel, Field   

class Payment(BaseModel):
    payment_id: str
    ride_id: str = Field(...,max_length=5, description="ID of the ride being paid for")
    user_id: str  = Field(..., description="ID of the user making the payment")
    amount: float = Field(..., gt=0, description="Payment amount, must be greater than zero")
    payment_method: str
    payment_status: str = Field(default="Pending")  # e.g., Pending, Completed, Failed
    transaction_id: str = None  # Optional field for transaction reference                                              