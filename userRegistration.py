registered_users = []
failed_registrations = []


def validate_name(name: str) -> bool:
    return len(name) > 3


def validate_email(email: str) -> bool:
    return "@" in email and "." in email


def validate_password(password: str) -> bool:
    return (
        any(char.isalpha() for char in password)
        and any(char.isnumeric() for char in password)
        and len(password) >= 8
    )


def validate_user_data(name: str, email: str, password: str) -> bool:
    return validate_name(name) and validate_email(email) and validate_password(password)


def create_user_account(name: str, email: str, password: str):
    user = {"name": name, "email": email, "password": password}

    if not validate_user_data(name, email, password):
        failed_registrations.append(user)
        raise ValueError("Invalid data")
    if any(u["email"] == email for u in registered_users):
        failed_registrations.append(user)
        raise ValueError("Email already exists")

    registered_users.append(user)
    return user


test_cases = [
    ("Alice", "alice@test.com", "Password123"),
    ("Al", "alice@test.com", "Password123"),
    ("Bob", "bobtest.com", "Password123"),
    ("Charlie", "charlie@test.com", "short"),
    ("Dave", "dup@test.com", "Password123"),
    ("Eve", "dup@test.com", "Password456"),
]

for name, email, password in test_cases:
    try:
        user = create_user_account(name, email, password)
        print(f"Registered: {user}")
    except ValueError as e:
        print(f"Failed for {email}: {e}")
