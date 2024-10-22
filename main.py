from fastapi import FastAPI, HTTPException, UploadFile, File
from task.router import router as task_router

app = FastAPI()

app.include_router(task_router)
