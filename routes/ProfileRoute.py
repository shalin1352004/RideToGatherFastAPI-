from fastapi import APIRouter, UploadFile, File, Form
from controllers.ProfileController import upload_profile_image, get_profile

router = APIRouter()

@router.post("/upload-profile-image/")
async def upload_image(
    user_id: str = Form(...),
    name: str = Form(...),
    email: str = Form(...),
    file: UploadFile = File(...)
):
    return await upload_profile_image(user_id, name, email, file)

@router.get("/profile/{user_id}")
async def read_profile(user_id: str):
    return await get_profile(user_id)
