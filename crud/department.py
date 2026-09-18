from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.department import Department
from app.schemas.department import DepartmentCreate


def create_department(
    db: Session,
    department: DepartmentCreate
):
    db_department = Department(
        name=department.name,
        description=department.description
    )

    db.add(db_department)
    db.commit()
    db.refresh(db_department)

    return db_department


def get_departments(db: Session):
    result = db.execute(
        select(Department)
    )

    return result.scalars().all()


def get_department(
    db: Session,
    department_id: int
):
    return db.get(
        Department,
        department_id
    )


def delete_department(
    db: Session,
    department_id: int
):
    department = db.get(
        Department,
        department_id
    )

    if department:
        db.delete(department)
        db.commit()

    return department