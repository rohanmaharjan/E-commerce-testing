import uuid


def unique_email(prefix="qa"):
    return f"{prefix}.{uuid.uuid4().hex[:10]}@example.com"


def new_user_payload(email=None, password="Str0ng!Pass#2026"):
    return {
        "first_name": "Test",
        "last_name": "User",
        "dob": "1990-01-15",
        "phone": "0612345678",
        "email": email or unique_email(),
        "password": password,
        "address": {
            "street": "Test Street 1",
            "city": "Kathmandu",
            "state": "Bagmati",
            "country": "NP",
            "postal_code": "44600",
        },
    }