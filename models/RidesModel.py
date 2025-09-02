from pydantic import BaseModel

class Ride(BaseModel):
    ride_id: str
    driver_name: str
    origin: str
    destination: str
    departure_time: str
    available_seats: int
    price_per_seat: float
    vehicle_info: str
    additional_details: str = None 
    
                                                                     