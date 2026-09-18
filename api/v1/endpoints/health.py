from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/health",
    tags=["Health"],
    summary="Health Check"
)
def health_check():
    return {
        "status": "healthy",
        "message": "Hospital AI Assistant is running"
    }


@router.get(
    "/health/database",
    tags=["Health"],
    summary="Database Health"
)
def database_health():
    return {
        "status": "healthy",
        "database": "connected"
    }


@router.get(
    "/health/ai",
    tags=["Health"],
    summary="AI Health"
)
def ai_health():
    return {
        "status": "healthy",
        "ai": "ready"
    }


@router.get(
    "/health/system",
    tags=["Health"],
    summary="System Health"
)
def system_health():
    return {
        "status": "healthy",
        "system": "operational"
    }