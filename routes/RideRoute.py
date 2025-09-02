from fastapi import APIRouter
from controllers.RideController import create_ride
from models.RidesModel import Ride  

router = APIRouter()

@router.post("/rides/")
async def add_ride(ride: Ride):  
    return await create_ride(ride)  
