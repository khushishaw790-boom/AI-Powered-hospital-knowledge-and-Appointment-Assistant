from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    doctors: Mapped[list["Doctor"]] = relationship(
        back_populates="department"
    )


class Doctor(Base):
    __tablename__ = "doctors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    specialization: Mapped[str] = mapped_column(String(150))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    phone: Mapped[str | None] = mapped_column(String(20), nullable=True)

    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id")
    )

    department: Mapped["Department"] = relationship(
        back_populates="doctors"
    )

    appointments: Mapped[list["Appointment"]] = relationship(
        back_populates="doctor"
    )


class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str | None] = mapped_column(
        String(255),
        unique=True,
        nullable=True
    )
    phone: Mapped[str] = mapped_column(String(20))

    date_of_birth: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    appointments: Mapped[list["Appointment"]] = relationship(
        back_populates="patient"
    )


class Appointment(Base):
    __tablename__ = "appointments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    doctor_id: Mapped[int] = mapped_column(
        ForeignKey("doctors.id")
    )

    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.id")
    )

    appointment_time: Mapped[datetime] = mapped_column(DateTime)

    status: Mapped[str] = mapped_column(
        String(50),
        default="scheduled"
    )

    reason: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    doctor: Mapped["Doctor"] = relationship(
        back_populates="appointments"
    )

    patient: Mapped["Patient"] = relationship(
        back_populates="appointments"
    )