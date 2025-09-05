from fastapi import FastAPI
from routes.RideRoute import router as ride_router
from starlette.middleware.cors import CORSMiddleware
from routes.DriverRoute import router as driver_router
from routes.PaymentRoute import router as payment_router
from routes.ProfileRoute import router as profile_router
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
        
            
    )

app.include_router(ride_router)
app.include_router(driver_router)
app.include_router(payment_router)
app.include_router(profile_router)
@app.get("/")
async def root():
    return {"message": "Welcome to RideToGather API"}