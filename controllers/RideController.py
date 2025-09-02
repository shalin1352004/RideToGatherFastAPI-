from models.RidesModel import Ride
from config.database import rides_collection

async def create_ride(ride:Ride):
    ride_dict = ride.dict()
    result = await rides_collection.insert_one(ride_dict)
    
    
    print("Driver Name:", ride.driver_name)
    return {"ride_id": str(result.inserted_id), "message": "Ride created successfully"  }