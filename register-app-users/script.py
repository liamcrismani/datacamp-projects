def validate_user(name: str, email: str, password: str) -> bool | None:
    if validate_name(name):
        pass
    else:
        raise ValueError("Name must be greater than two characters\
             and contain letters only.")
    if validate_email(email):
        pass
    else:
        raise ValueError("Invalid email format.")
    if validate_password(password):
        pass
    else:
        raise ValueError("Invalid password format.")
    return True


def register_user(name: str, email: str, password: str) -> dict[str] | bool:
    if validate_user(name, email, password):
        user = {'name': name, 'email': email, 'password': password}
        return user
    else:
        return False
