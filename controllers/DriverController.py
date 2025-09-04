from models.DriverModel import Driver
from config.database import drivers_collection

async def create_driver(driver:Driver):
    driver_dict = driver.dict()
    result = await drivers_collection.insert_one(driver_dict)
    
    return {"driver_id": str(result.inserted_id), "message": "Driver created successfully"  }   

def convert_id(Driver):
    Driver["_id"] = str(Driver["_id"])
    return Driver



async def get_driver(age:int):
    cursor = await drivers_collection.find({"age": {"$gte": age}}).to_list(length=100)
    return [convert_id(driver) for driver in cursor]

