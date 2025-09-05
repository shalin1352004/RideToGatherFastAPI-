from motor.motor_asyncio import AsyncIOMotorClient

client=AsyncIOMotorClient("mongodb://localhost:27017")
db=client["ridetogather_db"]

rides_collection=db["rides"]
drivers_collection=db["drivers"]
payments_collection=db["payments"]
profiles_collection=db["profiles"]

from fastapi import UploadFile,File
from cloudinary import CloudinaryImage
import cloudinary
cloudinary.config(
    cloud_name = "dhqb6c8y4",
    api_key = "651441796887498",
    api_secret = "_RpinSzbJ6D8GAI_R-yqnV0yZuQ"

)
