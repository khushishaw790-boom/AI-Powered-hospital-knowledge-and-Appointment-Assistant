departments = [
    {
        "id": 1,
        "name": "Cardiology",
        "description": "Heart and cardiovascular care"
    },
    {
        "id": 2,
        "name": "Neurology",
        "description": "Brain and nervous system care"
    },
    {
        "id": 3,
        "name": "Orthopedics",
        "description": "Bones, joints and muscles care"
    }
]


doctors = [
    {
        "id": 1,
        "name": "Dr. Amit Sharma",
        "specialization": "Cardiologist",
        "department_id": 1
    },
    {
        "id": 2,
        "name": "Dr. Priya Das",
        "specialization": "Neurologist",
        "department_id": 2
    },
    {
        "id": 3,
        "name": "Dr. Rahul Roy",
        "specialization": "Orthopedic Surgeon",
        "department_id": 3
    }
]


patients = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "9876543210"
    },
    {
        "id": 2,
        "name": "Jane Doe",
        "email": "jane@example.com",
        "phone": "9876543211"
    }
]


appointments = [
    {
        "id": 1,
        "doctor_id": 1,
        "patient_id": 1,
        "appointment_time": "2026-09-15 10:00",
        "status": "scheduled",
        "reason": "Regular heart checkup"
    },
    {
        "id": 2,
        "doctor_id": 2,
        "patient_id": 2,
        "appointment_time": "2026-09-15 11:00",
        "status": "scheduled",
        "reason": "Neurology consultation"
    }
]

users = [
    {
        "id": 1,
        "name": "Khushi",
        "email": "khushi@example.com",
        "password": "123456",
        "role": "patient"
    }
]