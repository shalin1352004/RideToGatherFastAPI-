from motor.motor_asyncio import AsyncIOMotorClient

client=AsyncIOMotorClient("mongodb://localhost:27017")
db=client["ridetogather_db"]

rides_collection=db["rides"]
drivers_collection=db["drivers"]
payments_collection=db["payments"]