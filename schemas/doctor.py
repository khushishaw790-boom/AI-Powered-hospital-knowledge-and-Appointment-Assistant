from pydantic import BaseModel


class DoctorCreate(BaseModel):
    name: str
    email: str
    specialization: str
    department_id: int


class DoctorResponse(BaseModel):
    id: int
    name: str
    email: str
    specialization: str
    department_id: int