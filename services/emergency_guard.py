def is_emergency(
    question: str
) -> bool:

    emergency_keywords = [
        "heart attack",
        "can't breathe",
        "cannot breathe",
        "severe bleeding",
        "unconscious",
        "stroke",
        "chest pain"
    ]

    question = question.lower()

    return any(
        word in question
        for word in emergency_keywords
    )


def emergency_response():

    return (
        "This may be an emergency. "
        "Please contact your local emergency "
        "services or go to the nearest emergency "
        "department immediately."
    )