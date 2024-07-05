# Preloaded data for validating email domain.
top_level_domains = [
    ".org",
    ".net",
    ".edu",
    ".ac",
    ".gov",
    ".com",
    ".io"
]


def validate_name(name: str) -> bool:
    if type(name) is str and len(name) > 2:
        return True
    else:
        return False


def validate_email(email: str) -> bool:
    if email.endswith(tuple(top_level_domains)) and '@' in email:
        return True
    else:
        return False
