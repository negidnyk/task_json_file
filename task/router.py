from fastapi import APIRouter, UploadFile, File
from task.services import sound_by_animal_from_file

router = APIRouter(
    prefix="/task",
    tags=["Task"]
)


@router.post("/animal_sound")
async def sound_by_animal(file: UploadFile = File(...)):
    return await sound_by_animal_from_file(file)
