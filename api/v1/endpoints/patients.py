from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_patients():
    return {
        "patients": [
            {
                "id": 1,
                "name": "Patient One",
                "age": 30
            },
            {
                "id": 2,
                "name": "Patient Two",
                "age": 45
            }
        ]
    }

@router.get("/{patient_id}")
def get_patient(patient_id: int):
    return {
        "patient_id": patient_id
    }


@router.post("/")
def create_patient():
    return {
        "message": "Patient created successfully"
    }


@router.put("/{patient_id}")
def update_patient(patient_id: int):
    return {
        "message": "Patient updated successfully",
        "patient_id": patient_id
    }


@router.delete("/{patient_id}")
def delete_patient(patient_id: int):
    return {
        "message": "Patient deleted successfully",
        "patient_id": patient_id
    }