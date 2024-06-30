def validate_user(name: str, email: str, password: str) -> bool | None:
    """ Checks users inputs are of correct types.

    Args:
      name: str: User name
      email: str: User email address. Only certain domains allowed.
      See top_level_domains in python_functions.py
      password: str: User password.

    Returns:
      True if all inputs are correct type, else None.
    """
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


def register_user(name: str, email: str, password: str) -> dict | bool:
    """ Stores the user details.

    Args:
      name: str: User name.
      email: str: User email address.
      password: str: User password.

    Returns:
      user: dict: Stores user details in key value pairs.
    """
    if validate_user(name, email, password):
        user: dict = {'name': name, 'email': email, 'password': password}
        return user
    else:
        return False
