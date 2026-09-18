from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_doctors():
    return {
        "doctors": [
            {
                "id": 1,
                "name": "Dr. Sharma",
                "department": "Cardiology"
            },
            {
                "id": 2,
                "name": "Dr. Verma",
                "department": "Neurology"
            },
            {
                "id": 3,
                "name": "Dr. Singh",
                "department": "Orthopedics"
            }
        ]
    }

@router.get("/{doctor_id}")
def get_doctor(doctor_id: int):
    return {
        "doctor_id": doctor_id
    }


@router.get("/department/{department_id}")
def get_doctors_by_department(department_id: int):
    return {
        "department_id": department_id,
        "doctors": []
    }


@router.post("/")
def create_doctor():
    return {
        "message": "Doctor created successfully"
    }


@router.put("/{doctor_id}")
def update_doctor(doctor_id: int):
    return {
        "message": "Doctor updated successfully",
        "doctor_id": doctor_id
    }


@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: int):
    return {
        "message": "Doctor deleted successfully",
        "doctor_id": doctor_id
    }