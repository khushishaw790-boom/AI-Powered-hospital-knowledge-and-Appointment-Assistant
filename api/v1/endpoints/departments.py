from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_departments():
    return {
        "departments": [
            "Cardiology",
            "Neurology",
            "Orthopedics",
            "Pediatrics"
        ]
    }


@router.get("/{department_id}")
def get_department(department_id: int):
    return {
        "department_id": department_id,
        "name": "Cardiology"
    }


@router.post("/")
def create_department():
    return {
        "message": "Department created successfully"
    }


@router.put("/{department_id}")
def update_department(department_id: int):
    return {
        "message": "Department updated successfully",
        "department_id": department_id
    }


@router.delete("/{department_id}")
def delete_department(department_id: int):
    return {
        "message": "Department deleted successfully",
        "department_id": department_id
    }