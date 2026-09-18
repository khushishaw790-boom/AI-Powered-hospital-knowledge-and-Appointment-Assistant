from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.api.v1.api import api_router


app = FastAPI(
    title="AI-Powered Hospital Knowledge and Appointment Assistant"
)


# API routes
app.include_router(
    api_router,
    prefix="/api/v1"
)


# Frontend static files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# Home page
@app.get("/")
async def home():
    return FileResponse("static/index.html")


# Health check
@app.get("/health")
async def health():
    return {
        "status": "ok"
    }

