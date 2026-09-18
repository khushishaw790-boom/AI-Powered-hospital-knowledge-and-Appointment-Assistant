from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate


def create_doctor(
    db: Session,
    doctor: DoctorCreate
):
    db_doctor = Doctor(
        name=doctor.name,
        email=doctor.email,
        specialization=doctor.specialization,
        department_id=doctor.department_id
    )

    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)

    return db_doctor


def get_doctors(db: Session):
    result = db.execute(
        select(Doctor)
    )

    return result.scalars().all()


def get_doctor(
    db: Session,
    doctor_id: int
):
    return db.get(Doctor, doctor_id)