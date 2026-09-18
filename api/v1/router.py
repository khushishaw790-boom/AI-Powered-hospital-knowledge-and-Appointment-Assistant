from fastapi import APIRouter

# ============================================================
# IMPORT ALL ENDPOINT ROUTERS
# ============================================================

from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.chat import router as chat_router
from app.api.v1.endpoints.departments import router as departments_router
from app.api.v1.endpoints.doctors import router as doctors_router
from app.api.v1.endpoints.patients import router as patients_router
from app.api.v1.endpoints.appointments import router as appointments_router
from app.api.v1.endpoints.health import router as health_router
from app.api.v1.endpoints.documents import router as documents_router
from app.api.v1.endpoints.indexing import router as indexing_router
from app.api.v1.endpoints.users import router as users_router





# ============================================================
# MAIN API ROUTER
# ============================================================

api_router = APIRouter()


# ============================================================
# AUTHENTICATION
# ============================================================

api_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"],
)


# ============================================================
# CHAT / AI ASSISTANT
# ============================================================

api_router.include_router(
    chat_router,
    prefix="/chat",
    tags=["Chat"],
)


# ============================================================
# DEPARTMENTS
# ============================================================

api_router.include_router(
    departments_router,
    prefix="/departments",
    tags=["Departments"],
)


# ============================================================
# DOCTORS
# ============================================================

api_router.include_router(
    doctors_router,
    prefix="/doctors",
    tags=["Doctors"],
)


# ============================================================
# PATIENTS
# ============================================================

api_router.include_router(
    patients_router,
    prefix="/patients",
    tags=["Patients"],
)


# ============================================================
# APPOINTMENTS
# ============================================================

api_router.include_router(
    appointments_router,
    prefix="/appointments",
    tags=["Appointments"],
)

api_router.include_router(
    health_router,
    prefix="/health",
    tags=["Health"],
)


# ============================================================
# DOCUMENTS
# ============================================================

api_router.include_router(
    documents_router,
    prefix="/documents",
    tags=["Documents"],
)


# ============================================================
# INDEXING / RAG
# ============================================================

api_router.include_router(
    indexing_router,
    prefix="/indexing",
    tags=["Indexing"],
)

api_router.include_router(
    auth_router,
    prefix="/users",
    tags=["Users"],
)


