def is_medical_question(
    question: str
) -> bool:

    medical_keywords = [
        "doctor",
        "hospital",
        "medicine",
        "treatment",
        "disease",
        "symptom",
        "appointment",
        "department"
    ]

    question = question.lower()

    return any(
        word in question
        for word in medical_keywords
    )