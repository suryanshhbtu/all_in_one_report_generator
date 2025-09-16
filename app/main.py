from fastapi import FastAPI
from app.routers import student_router

app = FastAPI(title="Student XML API", version="1.0.0")

# Register routers
app.include_router(student_router.router, prefix="/api", tags=["Student"])
