from models.DriverModel import Driver
from config.database import drivers_collection      
from fastapi import APIRouter
from controllers.DriverController import create_driver, get_driver              

router = APIRouter()

@router.post("/create-drivers/")
async def add_driver(driver: Driver):  
    return await create_driver(driver)

@router.get("/drivers/")
async def fetch_drivers(age: int = 0):
    return await get_driver(age) 