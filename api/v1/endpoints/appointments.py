from fastapi import APIRouter, HTTPException

from app.schemas.appointment import (
    AppointmentCreate,
    AppointmentResponse,
)
from app.crud.data import appointments


router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"],
)


@router.get("/", response_model=list[AppointmentResponse])
def get_appointments():
    return appointments


@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(appointment_id: int):

    for appointment in appointments:
        if appointment["id"] == appointment_id:
            return appointment

    raise HTTPException(
        status_code=404,
        detail="Appointment not found",
    )


@router.post("/", response_model=AppointmentResponse)
def create_appointment(data: AppointmentCreate):

    new_id = len(appointments) + 1

    appointment = {
        "id": new_id,
        "patient_id": data.patient_id,
        "doctor_id": data.doctor_id,
        "appointment_time": data.appointment_time,
        "status": data.status,
    }

    appointments.append(appointment)

    return appointment

@router.get("/{appointment_id}")
def get_appointment(appointment_id: int):
    return {
        "appointment_id": appointment_id
    }


@router.post("/")
def create_appointment():
    return {
        "message": "Appointment created successfully"
    }


@router.put("/{appointment_id}")
def update_appointment(appointment_id: int):
    return {
        "message": "Appointment updated successfully",
        "appointment_id": appointment_id
    }


@router.delete("/{appointment_id}")
def delete_appointment(appointment_id: int):
    return {
        "message": "Appointment deleted successfully",
        "appointment_id": appointment_id
    }