from models.ProfileModel import Profile
from config.database import profiles_collection, cloudinary
from fastapi import UploadFile, File
import cloudinary.uploader

async def upload_profile_image(user_id: str, name: str, email: str, file: UploadFile = File(...)):
    # Upload image to Cloudinary
    result = cloudinary.uploader.upload(file.file)
    image_url = result.get("secure_url")
    
    # Create profile dict
    profile_dict = {
        "user_id": user_id,
        "name": name,
        "email": email,
        "image_url": image_url
    }
    
    # Insert into MongoDB
    result = await profiles_collection.insert_one(profile_dict)
    
    return {"profile_id": str(result.inserted_id), "image_url": image_url, "message": "Profile created successfully"}

def convert_id(profile):
    profile["_id"] = str(profile["_id"])
    return profile

async def get_profile(user_id: str):
    profile = await profiles_collection.find_one({"user_id": user_id})
    if profile:
        return convert_id(profile)
    return {"message": "Profile not found"}
