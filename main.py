from fastapi import FastAPI
from routes.RideRoute import router as ride_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
        
            
    )

app.include_router(ride_router)

@app.get("/")
async def root():
    return {"message": "Welcome to RideToGather API"}