from datetime import datetime

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.id")
    )

    doctor_id: Mapped[int] = mapped_column(
        ForeignKey("doctors.id")
    )

    appointment_time: Mapped[datetime] = mapped_column()

    status: Mapped[str] = mapped_column(
        String(50),
        default="scheduled"
    )